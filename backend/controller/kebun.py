from setup.postgresql import db
from flask_jwt_extended import jwt_required
from flask import request
import traceback

class Kebun():
    def __init__(self) -> None:
        pass
    
    # @jwt_required()
    def get_all(self):
        try:
            hasil = db.query(query="select * from kebun")
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data kebun")
            traceback.print_exc()
            return "Error", 500
        
    def get_all_by_user_id(self, user_id):
        try:
            hasil = db.query(query="select id, nama, alamat from kebun where id_user = %s", params=(user_id,))
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data kebun by id user")
            traceback.print_exc()
            return "Error", 500
    
    def get_one(self, id):
        try:
            hasil = db.query(query="select id, nama, alamat from kebun where id = %s", params=(id,))
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get one data kebun")
            traceback.print_exc()
            return "Error", 500
        
    def add(self):
        try:
            data = request.json
            print(data)
            hasil = db.query(query="insert into kebun(nama, alamat, id_user) values(%s, %s, %s) returning *", params=(
                data.get("nama"),
                data.get("alamat"),
                data.get("id_user")["isi"],
            ))
            return {
                "berhasil": True,
                "hasil": hasil
            }
        except Exception as e:
            print(f"Error di add kebun")
            traceback.print_exc()
            return "Error internal server", 500
        
    def update(self):
        try:
            data = request.json
            print(f"data: {data}")
            db.query(query="update kebun set nama = %s, alamat = %s where id = %s", params=(
                data.get("nama"),
                data.get("alamat"),
                data.get("id"),
            ))
            return {
                "berhasil": True 
            }
        except Exception as e:
            print(f"Error di update data kebun: {e}")
            traceback.print_exc()
            return {
                "pesan": "error"
            }, 500
            
    def delete(self, id):
        try:
            db.query(query="delete from kebun where id = %s", params=(id,))
            return {
                "berhasil": True
            }
        except Exception as e:
            print(f"Error di delete kebun")
            traceback.print_exc()
            return {
                "pesan": "Error internal server"    
            }, 500
  
kebun = Kebun()