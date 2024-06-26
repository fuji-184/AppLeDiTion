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

    def classify_image(self, image_path):
        # Load and preprocess the image
        image = Image.open(image_path)
        image = self.transform(image).unsqueeze(0).numpy()

        # Run inference
        ort_inputs = {self.model_onnx.get_inputs()[0].name: image}
        ort_outs = self.model_onnx.run(None, ort_inputs)
        predicted_class_index = int(ort_outs[0].argmax())
        if predicted_class_index < len(self.class_list):
            return self.class_list[predicted_class_index]
        else:
            return 'Unknown'

    def generate_heatmap2(self, image_path, save_path):
        # Load and preprocess the image
        image = Image.open(image_path)
        transformed_image = self.transform(image).unsqueeze(0)  # shape: [1, 3, 224, 224]
        image_np = transformed_image.numpy()

        # Get the input name and shape for the ONNX model
        input_name = self.model_onnx.get_inputs()[0].name

        # Run the model to get the output logits
        ort_inputs = {input_name: image_np}
        ort_outs = self.model_onnx.run(None, ort_inputs)
        logits = ort_outs[0]

        # Convert logits to probabilities
        probs = torch.softmax(torch.from_numpy(logits), dim=1)
        top_prob, top_class = probs.topk(1, dim=1)
        predicted_class_index = top_class.item()

        # Backpropagation to get gradients
        self.model_onnx.predicted_class = predicted_class_index
        self.model_onnx.transforms_image = transformed_image.requires_grad

        # Clear previous gradients
        self.model_onnx.zero_grad()

        # Backward pass
        logits.backward()

        # Get the gradients for the feature map and take average across channels
        gradients = self.model_onnx.predicted_class.grad
        pooled_gradients = torch.mean(gradients, dim=[0, 2, 3])

        # Get the feature map of the last convolutional layer
        feature_map = self.model_onnx.transforms_image[0]
        feature_map = feature_map.detach().numpy()

        # Weighted average of the feature map using the gradients
        for i in range(gradients.shape[1]):
            feature_map[i, :, :] *= pooled_gradients[i]

        # Average the feature map along the channel dimension to get the heatmap
        heatmap = np.mean(feature_map, axis=0)
        heatmap = np.maximum(heatmap, 0)
        heatmap /= np.max(heatmap)

        # Resize heatmap to match the original image size
        heatmap = cv2.resize(heatmap, (image.size[1], image.size[0]))
        heatmap = np.uint8(255 * heatmap)

        # Apply heatmap to the original image
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

        # Superimpose heatmap on the original image
        superimposed_img = heatmap * 0.4 + np.array(image) * 0.6
        superimposed_img = superimposed_img.astype(np.uint8)

        # Save the superimposed image with heatmap
        cv2.imwrite(save_path, superimposed_img)

        return superimposed_img
       

    def generate_heatmap(self, image_path, save_path):
        # Load and preprocess the image
        image = Image.open(image_path)
        transformed_image = self.transform(image).unsqueeze(0)  # shape: [1, 3, 224, 224]
        image_np = transformed_image.numpy()

        # Get the input name for the ONNX model
        input_name = self.model_onnx.get_inputs()[0].name

        # Run the model to get the output logits
        ort_inputs = {input_name: image_np}
        ort_outs = self.model_onnx.run(None, ort_inputs)

        # Example: Get feature map from the last convolutional layer
        last_conv_output = ort_outs[0]  # Assuming this is the output of the last convolutional layer

        # Calculate gradient of the top predicted class with respect to the output of the last convolutional layer
        predicted_class_index = np.argmax(ort_outs[1])  # Assuming ort_outs[1] contains the predicted class scores
        gradients = self.compute_gradients(last_conv_output, predicted_class_index)

        # Calculate weighted average of the feature map
        weights = np.mean(gradients, axis=(2, 3), keepdims=True)
        heatmap = np.sum(weights * last_conv_output, axis=1, keepdims=True)

        # Normalize the heatmap
        heatmap = np.maximum(heatmap, 0)
        heatmap /= np.max(heatmap)

        # Resize heatmap to match the original image size
        heatmap = cv2.resize(heatmap[0], (image.size[0], image.size[1]))
        heatmap = np.uint8(255 * heatmap)

        # Apply heatmap to the original image
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

        # Superimpose heatmap on the original image
        superimposed_img = heatmap * 0.4 + np.array(image) * 0.6
        superimposed_img = superimposed_img.astype(np.uint8)

        # Save the superimposed image with heatmap
        cv2.imwrite(save_path, superimposed_img)

        return superimposed_img

    def compute_gradients(self, output, class_index):
        # Compute gradient of the top predicted class with respect to the output of the last convolutional layer
        gradients = np.zeros_like(output)
        gradients[:, class_index] = 1.0
        return gradients
