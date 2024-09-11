# controller.py

from flask import jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

jwt = JWTManager()

from setup.postgresql import db

@jwt_required(optional=True)
def daftar():
    id = get_jwt_identity()  # Mengambil identitas JWT jika ada
    
    if id:
      return {"pesan": "sudah login"}
    
    data = request.json
    print(data.get("nama"))
    
    if data:
        hasil = db.query(query="insert into users(nama, username, password, is_admin, tanggal_lahir) values(%s, %s, %s, %s, %s) returning id;", params=(
            data.get("nama"),
            data.get("username"),
            data.get("password"),
            data.get("is_admin"),
            data.get("tanggal_lahir"),
          )
        )
        
        print(f"id : {hasil}")
          
        token = create_access_token(hasil)

        return {
          "pesan": "berhasil",
          "id": hasil["id"],
          "nama": data.get("nama"),
          "token": token
        }
    else:
        return jsonify({"error": "Nama tidak ditemukan dalam data JSON"}), 400

@jwt_required(optional=True)
def masuk():
  id = get_jwt_identity()
  print(f"id : {id}")
  
  if id:
    return {"pesan": "sudah login"}
  
  data = request.json
  
  if data:
    hasil = db.query(query="select id, nama from users where username=%s and password=%s", params=(
      data.get("username"),
      data.get("password"),
     )
    )
    
    print(hasil[0]['id'])
    
    if hasil:
        token = create_access_token(identity=hasil[0]['id'])
        
        return {
          "pesan": "berhasil",
          "id": hasil[0]['id'],
          "nama": hasil[0]['nama'],
          "token": token
         }
  
  return {"pesan": "error"}
  
@jwt_required()
def keluar():
  res = jsonify({"pesan": "berhasil"})
  return res