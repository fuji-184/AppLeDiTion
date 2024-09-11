# # from flask import Flask
# from flask_socketio import SocketIO, emit
# import cv2
# import numpy as np
# import onnxruntime as ort
# import io
# from PIL import Image
# import traceback

# # app = Flask(__name__)
# socketio = SocketIO()

# # Muat model ONNX
# # ort_session = ort.InferenceSession('controller/yolov4.onnx')

# # def preprocess_image(image):
# #     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
# #     blob = cv2.dnn.blobFromImage(image, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)
# #     return blob

# # def postprocess_boxes(outputs, image_shape):
# #     # Post-process outputs untuk mendapatkan bounding boxes
# #     # Sesuaikan dengan format output model YOLOv4 ONNX
# #     return [], []  # placeholder untuk hasil

# @socketio.on('image')
# def handle_image(data):
#     print("Image received")
#     try:
#         # # Decode image
#         # image = Image.open(io.BytesIO(data))
#         # image = np.array(image)
        
#         # # Proses image
#         # blob = preprocess_image(image)
#         # ort_inputs = {ort_session.get_inputs()[0].name: blob}
#         # outputs = ort_session.run(None, ort_inputs)
        
#         # # Post-process results
#         # boxes, classes = postprocess_boxes(outputs, image.shape[:2])
        
#         # print("Processing complete")
        
#         # Kirim kembali hasil deteksi ke frontend
#         emit('result', {'boxes': 'boxes', 'classes': 'classes'})
#     except Exception as e:
#         print(f"Error processing image: {e}")
#         traceback.print_exc()

# # if __name__ == '__main__':
# #     socketio.run(app, debug=True)
