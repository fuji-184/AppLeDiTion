from flask import Flask, request
from setup.model import Model
from controller.pengobatan import obat
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "../model/efnetv2s.onnx")

class_list = ['apple_scab', 'black_rot', 'cedar_apple_rust', 'healthy']

model = Model(model_path, class_list)

def klasifikasi_route():
    try:
        if 'gambar' not in request.files:
            return {'err': 'Mohon upload gambar daun apel'}, 404

        gambar = request.files['gambar']
        path_gambar = os.path.join(current_dir, '../static/gambar.jpg')
        gambar.save(path_gambar)

        hasil_prediksi = model.classify_image(path_gambar)
        
        hasil_prediksi = obat(penyakit=hasil_prediksi)
        
        model.generate_heatmap(image_path=path_gambar, save_path='../static/heatmap.jpg')

        return {
            'hasil_prediksi': hasil_prediksi
        }

    except Exception as e:
        return {'error': str(e)}, 500
