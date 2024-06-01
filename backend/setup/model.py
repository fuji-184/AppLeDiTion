from torchvision import transforms
import onnxruntime
from PIL import Image
import numpy as np

class Model:
    def __init__(self, model_path, class_list):
        self.model_onnx = onnxruntime.InferenceSession(model_path)
        self.class_list = class_list

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ])

    def classify_image(self, image_path):
        image = Image.open(image_path)
        image = self.transform(image).unsqueeze(0).numpy()
        ort_inputs = {self.model_onnx.get_inputs()[0].name: image}
        ort_outs = self.model_onnx.run(None, ort_inputs)
        predicted_class_index = int(ort_outs[0].argmax())
        if predicted_class_index < len(self.class_list):
            return self.class_list[predicted_class_index]
        else:
            return 'Unknown'

    def generate_heatmap(self, image_path):
        # Code for generating heatmap
        pass
