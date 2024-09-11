from flask_socketio import SocketIO, emit
from setup.postgresql import db
import cv2
import numpy as np
import onnxruntime as ort
import io
from PIL import Image
import traceback

socketio = SocketIO()

@socketio.on('kirim_pesan')
def handle_message(data):
    print('Received message: ' + str(data))
    hasil = db.query(query="insert into chats(id_user, pesan) values(%s, %s) returning id", params=(data['id_user'], data['pesan'],))
    data['id'] = hasil['id']
    emit('pesan_diterima', data, broadcast=True)

ort_session = ort.InferenceSession('controller/yolov4.onnx')

def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    blob = cv2.dnn.blobFromImage(image, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)
    # Ubah urutan dimensi
    blob = np.transpose(blob, (0, 2, 3, 1))
    return blob


def save_blob_as_jpg(blob, file_name='output_image.jpg'):
    # Remove batch dimension (1, 3, 416, 416) -> (3, 416, 416)
    blob = np.squeeze(blob, axis=0)
    # Transpose back to (416, 416, 3)
    image = np.transpose(blob, (1, 2, 0))
    # Convert from float32 to uint8
    image = (image * 255).astype(np.uint8)
    # Convert BGR to RGB (since OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Save the image as JPG
    cv2.imwrite(file_name, image)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def postprocess_boxes(outputs, image_shape):
    # Anchor boxes untuk masing-masing skala
    anchor_boxes = [
        [(10, 13), (16, 30), (33, 23)],   # Anchors untuk skala 52x52
        [(30, 61), (62, 45), (59, 119)],  # Anchors untuk skala 26x26
        [(116, 90), (156, 198), (373, 326)]  # Anchors untuk skala 13x13
    ]
    
    boxes, confidences, classes = [], [], []

    # Ukuran grid untuk masing-masing skala
    grid_sizes = [52, 26, 13]

    for output, anchors, grid_size in zip(outputs, anchor_boxes, grid_sizes):
        for i in range(grid_size):
            for j in range(grid_size):
                for b in range(len(anchors)):
                    # Ambil parameter bounding box dari output
                    bx, by, bw, bh, obj_conf = output[0, i, j, b, :5]
                    class_probs = output[0, i, j, b, 5:]
                    
                    # Konversi ke koordinat absolut
                    x_center = (bx + j) / grid_size
                    y_center = (by + i) / grid_size
                    w = np.exp(bw) * anchors[b][0] / grid_size
                    h = np.exp(bh) * anchors[b][1] / grid_size
                    
                    # Konversi ke koordinat bounding box
                    x1 = (x_center - 0.5 * w) * image_shape[1]
                    y1 = (y_center - 0.5 * h) * image_shape[0]
                    x2 = (x_center + 0.5 * w) * image_shape[1]
                    y2 = (y_center + 0.5 * h) * image_shape[0]
                    
                    boxes.append([x1, y1, x2, y2])
                    confidences.append(obj_conf)
                    classes.append(np.argmax(class_probs))
    
    return boxes, classes, confidences

@socketio.on('image')
def handle_image(data):
    print("Image received")
    try:
        image = Image.open(io.BytesIO(data))
        image = np.array(image)
        
        # Preprocess image
        blob = preprocess_image(image)
        
        # Run inference
        ort_inputs = {ort_session.get_inputs()[0].name: blob}
        outputs = ort_session.run(None, ort_inputs)
        
        # # Post-process results 
        
        boxes, classes, confidences = postprocess_boxes(outputs, image.shape[:2])
        print(confidences)
     
        emit('result', {'boxes': 'boxes', 'classes': 'classes'})
    except Exception as e:
        print(f"Error di deteksi real time")
        traceback.print_exc()