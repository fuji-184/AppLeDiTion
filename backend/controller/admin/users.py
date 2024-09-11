from setup.postgresql import db
from flask_jwt_extended import jwt_required
from flask import request
import traceback

class Users():
    def __init__(self) -> None:
        pass
    
    # @jwt_required()
    def get_all(self):
        try:
            hasil = db.query(query="select id, username, nama, TO_CHAR(tanggal_lahir, 'YYYY-MM-DD') AS tanggal_lahir, is_admin from users")
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data users")
            traceback.print_exc()
            return "Error", 500
    
    def get_one(self, id):
        try:
            hasil = db.query(query="select id, username, nama, TO_CHAR(tanggal_lahir, 'YYYY-MM-DD') AS tanggal_lahir, is_admin from users where id = %s", params=(id,))
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get one data users")
            traceback.print_exc()
            return "Error", 500
        
    def add(self):
        try:
            data = request.json
            hasil = db.query(query="insert into users(nama, username, password, is_admin, tanggal_lahir) values(%s, %s, %s, %s, %s) returning *", params=(
                data.get("nama"),
                data.get("username"),
                data.get("password"),
                data.get("is_admin"),
                data.get("tanggal_lahir")
            ))
            return {
                "berhasil": True,
                "hasil": hasil
            }
        except Exception as e:
            print(f"Error di add users")
            traceback.print_exc()
            return "Error internal server", 500
        
    def update(self):
        try:
            data = request.json
            print(f"data: {data}")
            db.query(query="update users set is_admin = %s, nama = %s, username = %s, tanggal_lahir = %s where id = %s", params=(
                data.get("is_admin"),
                data.get("nama"),
                data.get("username"),
                data.get("tanggal_lahir"),
                data.get("id")
            ))
            return {
                "berhasil": True 
            }
        except Exception as e:
            print(f"Error di update data users: {e}")
            traceback.print_exc()
            return {
                "pesan": "error"
            }, 500
            
    def delete(self, id):
        try:
            db.query(query="delete from users where id = %s", params=(id,))
            return {
                "berhasil": True
            }
        except Exception as e:
            print(f"Error di delete users")
            traceback.print_exc()
            return {
                "pesan": "Error internal server"    
            }, 500
  
users = Users()