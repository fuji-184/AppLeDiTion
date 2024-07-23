import torch
import torch.nn as nn
from torchvision import transforms
import onnxruntime
from PIL import Image
import numpy as np
import cv2

class Model:
    def __init__(self, model_path, class_list):
        self.model_onnx = onnxruntime.InferenceSession(model_path)
        self.class_list = class_list

        # Preprocessing pipeline
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ])

        # Placeholder for feature maps and gradients
        self.feature_map = None
        self.gradients = None
        
    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=1, keepdims=True)

    def classify_image(self, image_path):
        # Load and preprocess the image
        image = Image.open(image_path)
        image = self.transform(image).unsqueeze(0).numpy()

        # Run inference
        ort_inputs = {self.model_onnx.get_inputs()[0].name: image}
        ort_outs = self.model_onnx.run(None, ort_inputs)
        score = self.softmax(ort_outs[0])
        # predicted_class_index = int(ort_outs[0].argmax())
        predicted_class_index = int(score.argmax())
        confidence_score = float(score[0][predicted_class_index]) * 100
        if predicted_class_index < len(self.class_list):
            return self.class_list[predicted_class_index], confidence_score
        else:
            return 'Unknown', 0
