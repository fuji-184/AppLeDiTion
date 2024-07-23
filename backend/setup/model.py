import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import cv2

from model.arsitektur import *

class Model:
    def __init__(self, model_path, class_list):
        self.model = EfficientNetV2(CONFIGS['s'], n_classes=4)  # Inisialisasi model

        # Muat state dict ke model
        state_dict = torch.load(model_path, map_location=torch.device('cpu'))
        self.model.load_state_dict(state_dict)
        
        # Panggil eval() pada model untuk menempatkannya ke mode evaluasi
        self.model.eval()
        self.class_list = class_list

        # Preprocessing pipeline
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ])

    def preprocess_image(self, image_path):
        image = Image.open(image_path)
        image = self.transform(image).unsqueeze(0)
        return image

    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=1, keepdims=True)

    def classify_image(self, image_path):
        # Preprocess the image
        image = self.preprocess_image(image_path)

        # Run inference
        with torch.no_grad():
            outputs = self.model(image)
            _, predicted = torch.max(outputs, 1)
            predicted_class_index = predicted.item()
            score = self.softmax(outputs.numpy())
            confidence_score = float(score[0][predicted_class_index]) * 100

        if predicted_class_index < len(self.class_list):
            return self.class_list[predicted_class_index], confidence_score
        else:
            return 'Unknown', 0

    def generate_heatmap(self, image_path, save_path):
        # Preprocess the image
        image = self.preprocess_image(image_path)

        # Forward pass to get feature map from 'pre' layer
        pre_layer_features = None
        def hook(module, input, output):
            nonlocal pre_layer_features
            pre_layer_features = output
        
        handle = self.model.features.register_forward_hook(hook)
        with torch.no_grad():
            _ = self.model(image)
        handle.remove()

        if pre_layer_features is None:
            raise ValueError("Failed to retrieve features from 'pre' layer")

        # Convert tensor to numpy array and reshape
        pre_layer_features_np = pre_layer_features.numpy()
        pre_layer_features_np = np.squeeze(pre_layer_features_np)  # Remove single-dimensional entries

        # Perform operations to create heatmap
        heatmap = np.mean(pre_layer_features_np, axis=0)  # Example: averaging along the channel axis
        heatmap = np.maximum(heatmap, 0)  # ReLU-like operation
        heatmap /= np.max(heatmap)  # Normalize

        # Resize heatmap to match input image size
        heatmap = cv2.resize(heatmap, (image.shape[3], image.shape[2]))

        # Apply heatmap to original image
        heatmap = cv2.applyColorMap(np.uint8(255 * heatmap), cv2.COLORMAP_JET)
        superimposed_img = heatmap * 0.4 + image.numpy().squeeze(0).transpose((1, 2, 0)) * 255
        superimposed_img = np.uint8(superimposed_img / np.max(superimposed_img) * 255)

        cv2.imwrite(save_path, superimposed_img)
        # return save_path
