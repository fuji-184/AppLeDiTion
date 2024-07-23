from flask import Flask, request
from setup.model import Model
from controller.pengobatan import obat
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "../model/EFS_99_eca_state_dict.pt")

class_list = ['apple_scab', 'black_rot', 'cedar_apple_rust', 'healthy']

model = Model(model_path, class_list)

def klasifikasi_route():
    try:
        if 'gambar' not in request.files:
            return {'err': 'Mohon upload gambar daun apel'}, 404

        gambar = request.files['gambar']
        path_gambar = os.path.join(current_dir, '../static/gambar.jpg')
        save_path = os.path.join(current_dir, '../static/heatmap.jpg')
        gambar.save(path_gambar)

        hasil_prediksi, confidence_score = model.classify_image(path_gambar)
        
        hasil_prediksi = obat(penyakit=hasil_prediksi)
        
        model.generate_heatmap(path_gambar, save_path)

        return {
            'hasil_prediksi': hasil_prediksi,
            'score': confidence_score,
            'heatmap': 'heatmap.jpg'
        }

    except Exception as e:
        return {'error': str(e)}, 500
