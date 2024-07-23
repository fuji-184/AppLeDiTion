import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np

from model.arsitektur import *

class Model:
    def __init__(self, model_path, class_list):
        self.model = EfficientNetV2(CONFIGS['s'], n_classes=4)
        self.model = torch.load(model_path, map_location=torch.device('cpu'))
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