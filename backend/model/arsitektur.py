import torch
from torch import nn

import torch.nn.functional as F

from einops import rearrange
from einops.layers.torch import Rearrange

class Conv2d(nn.Module):
  def __init__(self, in_chan, out_chan, kernel_size=3, padding=1, stride=1, groups=1, with_bn=True, with_act=True):
    super().__init__()
    self.conv = nn.Conv2d(in_chan, out_chan, kernel_size=kernel_size, stride=stride, padding=padding, groups=groups)
    self.with_bn = with_bn
    self.with_act = with_act

    if with_bn:
      self.bn = nn.BatchNorm2d(out_chan)

    if with_act:
      self.act = nn.SiLU()

  def forward(self, x):
    x = self.conv(x)

    if self.with_bn:
      x = self.bn(x)

    if self.with_act:
      x = self.act(x)

    return x

tes = Conv2d(3, 24)
params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(1, 3, 224, 224)
a = tes(input)

class StochasticDepth(nn.Module):
    def __init__(
        self,
        survival_prob = 0.8
    ):
        super(StochasticDepth, self).__init__()

        self.p =  survival_prob

    def forward(self, x):

        if not self.training:
            return x

        binary_tensor = torch.rand(x.shape[0], 1, 1, 1, device=x.device) < self.p

        return torch.div(x, self.p) * binary_tensor
    
class SE(nn.Module):
  def __init__(self, in_chan, r=4):
    super().__init__()
    self.squeeze = nn.AdaptiveAvgPool2d(1)
    self.excitation = nn.Sequential(
        nn.Conv2d(in_chan, int(in_chan//r), kernel_size=1, padding=0),
        nn.SiLU(),
        nn.Conv2d(int(in_chan//r), in_chan, kernel_size=1, padding=0),
        nn.Sigmoid()
    )

  def forward(self, x):

    input = x.clone()

    x = self.squeeze(x)
    x = self.excitation(x)

    return input * x

class Fused_MBConv(nn.Module):
  def __init__(self, in_chan, out_chan, kernel_size=3, stride=1, expansion=2, padding=1):
    super().__init__()
    self.skip_conn = (in_chan == out_chan) and (stride == 1)

    if expansion > 1:
      expansion = int(in_chan * expansion)
      self.conv = nn.Sequential(
          Conv2d(in_chan, expansion, kernel_size=kernel_size, stride=stride, padding=padding),
          SE(expansion),
          Conv2d(expansion, out_chan, kernel_size=1, padding=0, stride=1, with_act=False),
      )
    else:
      self.conv = nn.Sequential(
          Conv2d(in_chan, out_chan, kernel_size, stride=stride, padding=padding),
          SE(out_chan)
      )

    self.sd = StochasticDepth()

  def forward(self, x):

    residu = x.clone()

    x = self.conv(x)

    if self.skip_conn:
      x = self.sd(x)
      x = x + residu

    return x


tes = Fused_MBConv(22, 64*2, expansion=2)
params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(10, 22, 224, 224)
a = tes(input)

class MBConv(nn.Module):
  def __init__(self, in_chan, out_chan, kernel_size=3, stride=1, expansion=1, padding=1):
    super().__init__()
    self.skip_conn = (in_chan == out_chan) and (stride == 1)

    if expansion > 1:
      expansion = int(in_chan * expansion)
      self.conv = nn.Sequential(
          Conv2d(in_chan, expansion, kernel_size=1, padding=0, stride=1),
          Conv2d(expansion, expansion, kernel_size=kernel_size, stride=stride, padding=padding, groups=expansion),
          SE(expansion),
          Conv2d(expansion, out_chan, kernel_size=1, padding=0, stride=1, with_act=False)
      )
    else:
      self.conv = nn.Sequential(
          Conv2d(in_chan, in_chan, kernel_size=kernel_size, stride=stride, padding=padding, groups=in_chan),
          SE(in_chan),
          Conv2d(in_chan, out_chan, kernel_size=1, padding=0, stride=1, with_act=False)
      )

    self.sd = StochasticDepth()

  def forward(self, x):

    residu = x.clone()

    x = self.conv(x)

    if self.skip_conn:
      x = self.sd(x)
      x = x + residu

    return x

tes = MBConv(768, 768, expansion=0.5)
params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(10, 768, 16, 16)
a = tes(input)

class Embedding(nn.Module):
  def __init__(self, in_chan, embed_dim, kernel_size=8, stride=8, padding=0, expansion=1):
    super().__init__()
    self.conv = Fused_MBConv(in_chan, embed_dim, kernel_size=kernel_size, stride=stride, padding=padding)

  def forward(self, x):
    b, c, h, w = x.shape
    x = self.conv(x)
    x = rearrange(x, 'b c h w -> b (h w) c')

    return x

tes = Embedding(24, 768, kernel_size=8, stride=6, padding=0)
params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(1, 24, 224, 224)
a = tes(input)

class Repatch(nn.Module):
    def __init__(self, in_chan, out_chan, kernel_size=3, stride=2, padding=0):
        super().__init__()

        self.conv = MBConv(in_chan, out_chan, kernel_size=kernel_size, stride=stride, padding=padding)

    def forward(self, x):
      _, n, _ = x.shape
      h = w = int(n**0.5)
      x = rearrange(x, 'b (h w) c -> b c h w', h=h, w=w)

      x = self.conv(x)

      x = rearrange(x, 'b c h w -> b (h w) c')

      return x

tes = Repatch(192, 256, kernel_size=3, stride=2)
params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(10, 196, 192)
output = tes(input)
print(output.shape)

class Fused_MBConv_Layers(nn.Module):
    def __init__(self, in_chan, out_chan=None, kernel_size=3, stride=1, padding=1, expansion=1, jumlah=0, downsample=False):
        super().__init__()

        if jumlah > 0:
            fused_mbconv_layers = []
            for _ in range(jumlah):
                fused_mbconv_layers.append(Fused_MBConv(in_chan, in_chan, kernel_size=kernel_size, stride=stride, padding=padding, expansion=expansion))
            self.fused_mbconv = nn.Sequential(*fused_mbconv_layers)
        else:
            self.fused_mbconv = nn.Identity()

        self.out_chan = out_chan
        if downsample:
          stride = 2
        if out_chan is not None:
            self.up_chan = Fused_MBConv(in_chan, out_chan, kernel_size=kernel_size, stride=stride, padding=padding, expansion=expansion)

    def forward(self, x):

      x = self.fused_mbconv(x)

      if self.out_chan is not None:
        x = self.up_chan(x)

      return x

tes = Fused_MBConv_Layers(192, kernel_size=3, stride=1, expansion=2, jumlah=2)
params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(1, 192, 224, 224)
output = tes(input)
print(output.shape)

class MBConv_Layers(nn.Module):
    def __init__(self, in_chan, out_chan=None, kernel_size=3, stride=1, padding=1, expansion=1, jumlah=0):
        super().__init__()

        if jumlah > 0:
            mbconv_layers = []
            for _ in range(jumlah):
                mbconv_layers.append(MBConv(in_chan, in_chan, kernel_size=kernel_size, stride=stride, padding=padding, expansion=expansion))
            self.mbconv = nn.Sequential(*mbconv_layers)
        else:
            self.mbconv = nn.Identity()

        self.out_chan = out_chan
        if out_chan is not None:
            self.up_chan = MBConv(in_chan, out_chan, kernel_size=kernel_size, stride=stride, padding=padding, expansion=expansion)

    def forward(self, x):

      _, n, _ = x.shape
      h = w = int(n**0.5)
      x = rearrange(x, 'b (h w) c -> b c h w', h=h, w=w)

      x = self.mbconv(x)

      if self.out_chan is not None:
        x = self.up_chan(x)

      x = rearrange(x, 'b c h w -> b (h w) c')

      return x

tes = MBConv_Layers(192, kernel_size=3, stride=1, expansion=2, jumlah=2)
params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(10, 196, 192)
output = tes(input)
print(output.shape)

class MultiHeadAttention(nn.Module):
  def __init__(self, in_dim, num_heads=8, kernel_size=3, with_cls_token=False, dropout=0.1):
    super().__init__()
    padding = (kernel_size - 1)//2
    self.forward_conv = self.forward_conv
    self.num_heads = num_heads
    self.head_dim = in_dim // num_heads
    self.with_cls_token = with_cls_token
    self.conv = nn.Sequential(
        nn.Conv2d(in_dim, in_dim, kernel_size=1, padding=0),
        Rearrange('b c h w -> b (h w) c'),
    )
    self.att_drop = nn.Dropout(dropout)

  def forward_conv(self, x):
    B, hw, C = x.shape
    if self.with_cls_token:
      cls_token, x = torch.split(x, [1, hw-1], 1)
    H = W = int(x.shape[1]**0.5)
    x = rearrange(x, 'b (h w) c -> b c h w', h=H, w=W)

    q = self.conv(x)
    k = self.conv(x)
    v = self.conv(x)

    if self.with_cls_token:
            q = torch.cat((cls_token, q), dim=1)
            k = torch.cat((cls_token, k), dim=1)
            v = torch.cat((cls_token, v), dim=1)

    return q, k, v

  def forward(self, x):

    q, k, v = self.forward_conv(x)

    q = rearrange(x, 'b t (d H) -> b H t d', H=self.num_heads)
    k = rearrange(x, 'b t (d H) -> b H t d', H=self.num_heads)
    v = rearrange(x, 'b t (d H) -> b H t d', H=self.num_heads)

    att_score = q@k.transpose(2, 3)/self.num_heads**0.5
    att_score = F.softmax(att_score, dim=-1)
    att_score = self.att_drop(att_score)

    x = att_score@v

    x = rearrange(x, 'b H t d -> b t (H d)')

    return x, att_score

model = MultiHeadAttention(768, with_cls_token=True)

params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(1, 197, 768)
x, _ = model(input)
print(x.shape)

class Encoder(nn.Module):
  def __init__(self, embed_dim, num_heads=8, dropout=0.1):
    super().__init__()
    self.norm1 = nn.LayerNorm(embed_dim)
    self.mhsa = MultiHeadAttention(embed_dim, with_cls_token=False, dropout=dropout)
    self.dropout = nn.Dropout(dropout)
    self.norm2 = nn.LayerNorm(embed_dim)

    self.ffn = nn.Sequential(
        nn.Conv2d(embed_dim, int(embed_dim*2), kernel_size=1),
        nn.GELU(),
        nn.Dropout(dropout),
        nn.Conv2d(int(embed_dim*2), embed_dim, kernel_size=1),
        nn.Dropout(dropout),
    )

  def forward(self, x):

    residu = x.clone()

    x = self.norm1(x)

    x, attn_score = self.mhsa(x)

    x = residu + self.dropout(x)

    residu = x.clone()

    x = self.norm2(x)

    B, hw, C = x.shape

    H = W = int(x.shape[1]**0.5)
    x = rearrange(x, 'b (h w) c -> b c h w', h=H, w=W)

    x = self.ffn(x)

    x = rearrange(x, 'b c h w -> b (h w) c')

    x = residu + x

    return x, attn_score

tes = Encoder(768, num_heads=8)

params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(1, 196, 768)
a, _ = tes(input)

class Encoder_Layers(nn.Module):
  def __init__(self, embed_dim, num_heads=8, dropout=0.1, jumlah=0):
    super().__init__()
    if jumlah > 0:
      self.encoder_layers = nn.ModuleList([
            Encoder(embed_dim=embed_dim, num_heads=num_heads, dropout=dropout)
            for _ in range(jumlah)
        ])
    else:
      self.encoder_layers = nn.Identity()

  def forward(self, x):

    attn_scores = []
    for encoder in self.encoder_layers:
      x, attn_score = encoder(x)
      attn_scores.append(attn_score)

    return x, attn_scores

tes = Encoder_Layers(768, num_heads=8, jumlah=1)

params = sum(p.numel() for p in tes.parameters() if p.requires_grad)
print(f"total parameters: {params}")

input = torch.randn(1, 196, 768)
a, _ = tes(input)

class EfficientNetV2_VitEncoder(nn.Module):
  def __init__(self, embed_dim, num_heads, num_classes=4, patch_size=16, dropout=0.1):
    super().__init__()
    self.conv = nn.Sequential(
        Conv2d(3, 24, stride=2),
        Fused_MBConv(24, 32, stride=1, expansion=1),
    )
    self.embedding = Embedding(32, embed_dim, kernel_size=patch_size, stride=patch_size//2, padding=0)
    self.layers = nn.ModuleList([
        Encoder_Layers(embed_dim, num_heads=num_heads, dropout=dropout, jumlah=3),
        MBConv_Layers(embed_dim, kernel_size=3, padding=1, jumlah=6, expansion=2),

        Repatch(embed_dim, embed_dim*2, kernel_size=5, stride=2, padding=0),

        Encoder_Layers(embed_dim*2, num_heads=num_heads, dropout=dropout, jumlah=6),
        MBConv_Layers(embed_dim*2, kernel_size=3, padding=1, jumlah=6, expansion=2),

        Repatch(embed_dim*2, embed_dim*2*2, kernel_size=3, stride=1, padding=0),

        Encoder_Layers(embed_dim*2*2, num_heads=num_heads, dropout=dropout, jumlah=2),
    ])
    self.pool = nn.AdaptiveAvgPool1d(1)
    self.head = nn.Linear(embed_dim*2*2, num_classes)

  def forward(self, x):
    x = self.conv(x)
    x = self.embedding(x)
    n = x.shape[0]

    attn_scores = []

    for layer in self.layers:
      if isinstance(layer, Encoder_Layers):
        x, attn_score = layer(x)
        attn_scores.extend(attn_score)
      else:
        x = layer(x)
    x = rearrange(x, "b s d -> b d s")

    x = self.pool(x)
    x = x.squeeze(-1)

    x = self.head(x)
    attn_w = None

    return x

# model = EfficientNetV2_VitEncoder(embed_dim=192, num_heads=8, num_classes=4, patch_size=16)

# params = sum(p.numel() for p in model.parameters() if p.requires_grad)
# print(f"total parameters: {params}")

# input = torch.randn(10, 3, 224, 224)
# x = model(input)