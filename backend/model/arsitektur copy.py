import torch
from torch import nn, optim
from torchvision import transforms, datasets, models
import matplotlib.pyplot as plt
import os
from torch.utils.data import DataLoader
import numpy as np
import torch.nn.functional as F
from torch.utils.data import random_split, DataLoader
from torchvision import datasets, transforms

CONFIGS = {
    "s": {
        "widths": [24, 24, 48, 64, 128, 160, 256],
        "depths": [2, 4, 4, 6, 9, 15],
        "strides": [1, 2, 2, 2, 1, 2],
        "convs": [0, 1, 1, 2, 3, 3],
        "output_conv_size": 1280,
        "timm_weights": "tf_efficientnetv2_s"
    }
}


import torch
import torch.nn as nn

def conv_block(in_channels, out_channels, kernel_size=3, stride=1, padding=1, groups=1, bias=False, bn=True, act=True):
    layers = []

    if kernel_size == 1:
        # Standard convolution if kernel size is 1
        layers.append(nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, padding=padding, groups=groups, bias=bias))
    else:
        # Spatially separable convolution
        # First apply vertical convolution (kernel_size x 1)
        layers.append(nn.Conv2d(in_channels, in_channels, kernel_size=(kernel_size, 1), stride=stride,
                                padding=(padding, 0), groups=groups, bias=bias))
        # Then apply horizontal convolution (1 x kernel_size)
        layers.append(nn.Conv2d(in_channels, out_channels, kernel_size=(1, kernel_size), stride=1,
                                padding=(0, padding), groups=groups, bias=bias))

    if bn:
        layers.append(nn.BatchNorm2d(out_channels))
    if act:
        layers.append(nn.SiLU())

    return nn.Sequential(*layers)

class SEBlock(nn.Module):
    def __init__(self, c, r=24):
        super(SEBlock, self).__init__()
        self.squeeze = nn.AdaptiveMaxPool2d(1)
        self.excitation = nn.Sequential(
            nn.Conv2d(c, c // r, kernel_size=1),
            nn.SiLU(),
            nn.Conv2d(c // r, c, kernel_size=1),
            nn.Sigmoid()
        )
    def forward(self, x):
        s = self.squeeze(x)
        e = self.excitation(s)
        return x * e
    

import torch
from torch import nn
from torch.nn.parameter import Parameter

class eca_layer(nn.Module):
    """Constructs a ECA module.

    Args:
        channel: Number of channels of the input feature map
        k_size: Adaptive selection of kernel size
    """
    def __init__(self, channel, k_size=3):
        super(eca_layer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.conv = nn.Conv1d(1, 1, kernel_size=k_size, padding=(k_size - 1) // 2, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # x: input features with shape [b, c, h, w]
        b, c, h, w = x.size()

        # feature descriptor on the global spatial information
        y = self.avg_pool(x)

        # Two different branches of ECA module
        y = self.conv(y.squeeze(-1).transpose(-1, -2)).transpose(-1, -2).unsqueeze(-1)

        # Multi-scale information fusion
        y = self.sigmoid(y)

        return x * y.expand_as(x)
    
class FusedMBConv(nn.Module):
    def __init__(self, n_in, n_out, expansion, kernel_size=3, stride=1, r=24, dropout=0.1):
        super(FusedMBConv, self).__init__()
        self.skip_connection = (n_in == n_out) and (stride == 1)
        padding = (kernel_size-1)//2
        expanded = expansion*n_in

        self.expand_pw = conv_block(n_in, expanded, kernel_size=3, stride=stride, padding=1)
        self.reduce_pw = conv_block(expanded, n_out, kernel_size=1, padding=0, act=False)

        if expansion == 1:
            self.reduce_pw = nn.Identity()
            self.expand_pw = conv_block(n_in, n_out, kernel_size=3, stride=stride, padding=1)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        residual = x
        x = self.expand_pw(x)
        x = self.reduce_pw(x)
        if self.skip_connection:
            x = self.dropout(x)
            x = x + residual
        return x
    
class MBConv(nn.Module):
    def __init__(self, n_in, n_out, expansion, kernel_size=3, stride=1, r=24, dropout=0.1):
        super(MBConv, self).__init__()
        self.skip_connection = (n_in == n_out) and (stride == 1)

        padding = (kernel_size-1)//2
        expanded = expansion*n_in

        self.expand_pw = nn.Identity() if expansion == 1 else conv_block(n_in, expanded, kernel_size=1, padding=0)
        self.reduce_pw = conv_block(expanded, n_out, kernel_size=1, padding=0, act=False)

        #self.se = SEBlock(expanded, r=4 * expansion)
        self.se = eca_layer(channel=n_out)

        self.depthwise = conv_block(n_out, n_out, kernel_size=kernel_size, stride=stride, padding=padding, groups=n_out)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        residual = x

        x = self.expand_pw(x)
        x = self.reduce_pw(x)
        x = self.se(x)

        x = self.depthwise(x)
        if self.skip_connection:
            x = self.dropout(x)
            x = x + residual
        #print("output mbconv : ", x.shape)
        return x
    

def mbconv4(n_in, n_out, kernel_size=3, stride=1, r=24, dropout=0.1):
    return MBConv(n_in, n_out, 4, kernel_size=kernel_size, stride=stride, r=r, dropout=dropout)

def mbconv6(n_in, n_out, kernel_size=3, stride=1, r=24, dropout=0.1):
    return MBConv(n_in, n_out, 6, kernel_size=kernel_size, stride=stride, r=r, dropout=dropout)

def fused_mbconv1(n_in, n_out, kernel_size=3, stride=1, r=24, dropout=0.1):
    return FusedMBConv(n_in, n_out, 1, kernel_size=kernel_size, stride=stride, r=r, dropout=dropout)

def fused_mbconv4(n_in, n_out, kernel_size=3, stride=1, r=24, dropout=0.1):
    return FusedMBConv(n_in, n_out, 4, kernel_size=kernel_size, stride=stride, r=r, dropout=dropout)
def shuffle(nin, nout, kernel_size=3, stride=1, r=24, dropout=0.1):
    return ShuffleNetUnit(nin, nout)
def dynamic(n_in, n_out, kernel_size=3, stride=1, r=24, dropout=0.1):
    return HeterogeneousDynamicConvBlock(in_channels=n_in, out_channels=n_out)
layers_map = [fused_mbconv1, fused_mbconv4, mbconv4, mbconv6]

def create_stage(n_in, n_out, num_layers, layer=mbconv6,
                 kernel_size=3, stride=1, r=24, ps=0):
    layers = [layer(n_in, n_out, kernel_size=kernel_size,
                       stride=stride, r=r, dropout=ps)]
    layers += [layer(n_out, n_out, kernel_size=kernel_size,
                        r=r, dropout=ps) for _ in range(num_layers-1)]
    return nn.Sequential(*layers)

class EfficientNetV2(nn.Module):
    def __init__(self, cfg, n_classes=1000):
        super(EfficientNetV2, self).__init__()
        self.cfg = cfg
        self.n_classes = n_classes
        widths, depths, strides, convs = cfg['widths'],cfg['depths'],cfg['strides'],cfg['convs']
        outconv_size = cfg['output_conv_size']

        stages = [conv_block(3, widths[0], stride=2, padding=1)]
        for i in range(len(depths)):
            stages.append(create_stage(widths[i], widths[i + 1], depths[i], layer=layers_map[convs[i]],
                        stride=strides[i], r=4 if i ==0 else 24, ps=0))

        self.features = nn.Sequential(*stages)
        self.pre = conv_block(widths[-1], outconv_size, kernel_size=1, padding=0)
        self.pool_flatten = nn.Sequential(nn.AdaptiveAvgPool2d(1), nn.Flatten())

        self.head = nn.Sequential(
            nn.Linear(outconv_size, n_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.pre(x)
        x = self.pool_flatten(x)

        # Final linear layer
        x = self.head(x)
        # print("After head:", x.shape)
        return x
    
def efficientnetv2_s(n_classes=1000):
    return EfficientNetV2(CONFIGS['s'], n_classes=n_classes)
