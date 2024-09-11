from flask import Flask, request
from setup.model import Model
from controller.pengobatan import obat
import os
import traceback
import asyncio
from concurrent.futures import ThreadPoolExecutor

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "../model/efnetv2_vit_encoder_state_dict.pt")

class_list = ['apple_scab', 'black_rot', 'cedar_apple_rust', 'healthy']

model = Model(model_path, class_list)

async def klasifikasi_route():
    try:
        if 'gambar' not in request.files:
            return {'err': 'Mohon upload gambar daun apel'}, 404

        gambar = request.files['gambar']
        path_gambar = os.path.join(current_dir, '../static/gambar.jpg')
        save_path = os.path.join(current_dir, '../static/heatmap.jpg')
        gambar.save(path_gambar)

        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            # hasil_prediksi, confidence_score = await model.classify_image(path_gambar)
            hasil_prediksi, confidence_score = await loop.run_in_executor(executor, model.classify_image, path_gambar)
        
        detail = obat(penyakit=hasil_prediksi)
        
        loop2 = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            await loop2.run_in_executor(executor, model.generate_heatmap, path_gambar, save_path)
        
        # model.generate_heatmap(path_gambar, save_path)
        
        print(f"hasil: {hasil_prediksi}")
        return {
            'hasil_prediksi': hasil_prediksi,
            'score': confidence_score,
            'heatmap': 'heatmap.jpg',
            'id_hasil': detail[0]["id"],
            'deskripsi': detail[0]["deskripsi"],
            'pengobatan': detail[0]["pengobatan"]
        }

    except Exception as e:
        print(f"Error di klasifikasi")
        traceback.print_exc()
        return {'error': str(e)}, 500
