from setup.postgresql import db
from flask_jwt_extended import jwt_required
from flask import request
import traceback
import pytz
import re

def convert_to_wib(dt_obj):
    return dt_obj.astimezone(pytz.timezone('Asia/Jakarta'))\
        .strftime("%H:%M WIB, %a, %d %b %Y")
        
def ambil_src_gambar_pertama(html):
    img_regex = r'<img[^>]+src="([^">]+)"'
    match = re.search(img_regex, html)
    return match.group(1) if match else None

class Artikel():
    def __init__(self) -> None:
        pass
    
    # @jwt_required()
    def get_all(self):
        try:
            hasil = db.query(query="select id, judul, tanggal, thumbnail from artikel")
            for item in hasil:
                item['tanggal'] = convert_to_wib(item['tanggal'])
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data artikel")
            traceback.print_exc()
            return "Error", 500
    
    def get_one(self, id):
        try:
            hasil = db.query(query="select * from artikel where id = %s", params=(id,))
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get one data artikel")
            traceback.print_exc()
            return "Error", 500
        
    def get_one_by_judul(self, judul):
        try:
            hasil = db.query(query="select * from artikel where judul = %s", params=(judul,))
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get one data artikel")
            traceback.print_exc()
            return "Error", 500
        
    def add(self):
        try:
            data = request.json
            thumbnail = ambil_src_gambar_pertama(data.get("isi"))
            hasil = db.query(query="insert into artikel(judul, isi, thumbnail) values(%s, %s, %s) returning *", params=(
                data.get("judul"),
                data.get("isi"),
                thumbnail,
            ))
            return {
                "berhasil": True,
                "hasil": hasil
            }
        except Exception as e:
            print(f"Error di add artikel")
            traceback.print_exc()
            return "Error internal server", 500
        
    def update(self):
        try:
            data = request.json
            thumbnail = ambil_src_gambar_pertama(data.get("isi"))
            db.query(query="update artikel set judul = %s, isi = %s, thumbnail = %s where id = %s", params=(
                data.get("judul"),
                data.get("isi"),
                data.get("id"),
                thumbnail,
            ))
            return {
                "berhasil": True 
            }
        except Exception as e:
            print(f"Error di update data artikel: {e}")
            traceback.print_exc()
            return {
                "pesan": "error"
            }, 500
            
    def delete(self, id):
        try:
            db.query(query="delete from artikel where id = %s", params=(id,))
            return {
                "berhasil": True
            }
        except Exception as e:
            print(f"Error di delete artikel")
            traceback.print_exc()
            return {
                "pesan": "Error internal server"    
            }, 500
  
artikel = Artikel()