# controller.py

from flask import jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, set_access_cookies, get_jwt_identity, create_refresh_token, set_refresh_cookies, unset_jwt_cookies
from flask_cors import cross_origin

jwt = JWTManager()

@cross_origin()
@jwt_required(optional=True)
def daftar():
    # nama = get_jwt_identity()  # Mengambil identitas JWT jika ada
    # print(nama)
    data = request.json
    
    if data:
        token = create_access_token(identity=data)
        refresh_token = create_refresh_token(identity=data)
        res = jsonify({"tes": "berhasil"})
        set_access_cookies(res, token)
        set_refresh_cookies(res, refresh_token)
        # res.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")
        res.headers.add("Access-Control-Allow-Credentials", "true")
        return res
    else:
        return jsonify({"error": "Nama tidak ditemukan dalam data JSON"}), 400

@cross_origin()
@jwt_required()
def masuk():
  nama = get_jwt_identity()
  print(nama)
  res = jsonify({"pesan": "berhasil"})
  res.headers.add("Access-Control-Allow-Credentials", "true")
  return res
  
@cross_origin()
@jwt_required()
def keluar():
  res = jsonify({"pesan": "keluar"})
  unset_jwt_cookies(res)
  return res