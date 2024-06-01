from flask import request

def daftar():
  nama = request.json
  print(nama)
  return {"suskses"}