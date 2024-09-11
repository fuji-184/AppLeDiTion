from flask import Flask, Response
from flask_cors import CORS
from setup.websocket import socketio
from datetime import timedelta
from markupsafe import escape
import asyncio

from setup.postgresql import db

from controller.klasifikasi import klasifikasi_route
from controller.auth import jwt, daftar, masuk, keluar
from controller.pengobatan import obat
from controller.chat import ambilChat

from controller.admin.visitors import visitors
from controller.admin.users import users
from controller.admin.artikel import artikel
from controller.histori_deteksi import histori_deteksi
from controller.kebun import kebun

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "Fast And Focus"
# app.config['JWT_COOKIE_SECURE'] = False
# app.config['JWT_TOKEN_LOCATION'] = 'cookies'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
# app.config['JWT_CSRF_CHECK_FORM'] = True
# app.config['JWT_CSRF_IN_COOKIES'] = True
# app.config['JWT_COOKIE_CSRF_PROTECT'] = True
# app.config['JWT_COOKIE_DOMAIN'] = "127.0.0.1"
# app.config['JWT_SAME_SITE'] = "Lax"
# app.config['JWT_SESSION_COOKIE'] = False

CORS(app, supports_credentials=True, resources={
    r"/*": {
        "origins": ["*"]
    }
})

socketio.init_app(app, cors_allowed_origins="http://127.0.0.1:5173")
jwt.init_app(app)


@app.route('/')
def home():
    return 'home'

@app.route('/klasifikasi', methods=['POST'])
def klasifikasi():
    return asyncio.run(klasifikasi_route())
    
@app.route("/daftar", methods=['POST'])
def signup():
  return daftar()
  
@app.route("/masuk", methods=['POST'])
def login():
  return masuk()
  
@app.route("/keluar", methods=['POST'])
def logout():
  return keluar()
    
@app.route("/obat", methods=['GET'])
def pengobatan():
  return obat(penyakit="apple_scab")

@app.route("/chat", methods=["GET"])
def chat():
  return ambilChat()


# admin

# histori_deteksi
@app.route("/users", methods=["GET"])
def get_all_users():
  return users.get_all()

@app.route("/users/<id>", methods=["GET"])
def get_one_user(id):
  return users.get_one(escape(id))

@app.route("/users", methods=["POST"])
def add_users():
  return users.add()

@app.route("/users", methods=["PUT"])
def update_users():
  return users.update()

@app.route("/users/<id>", methods=["DELETE"])
def delete_users(id):
  return users.delete(escape(id))

# artikel
@app.route("/artikel", methods=["GET"])
def get_all_artikel():
  return artikel.get_all()

@app.route("/artikel/<id>", methods=["GET"])
def get_one_artikel(id):
  return artikel.get_one(escape(id))

@app.route("/artikel/by/<judul>", methods=["GET"])
def get_one_artikel_by_judul(judul):
  return artikel.get_one_by_judul(escape(judul))

@app.route("/artikel", methods=["POST"])
def add_artikel():
  return artikel.add()

@app.route("/artikel", methods=["PUT"])
def update_artikel():
  return artikel.update()

@app.route("/artikel/<id>", methods=["DELETE"])
def delete_artikel(id):
  return artikel.delete(escape(id))

@app.route("/visitors", methods=["GET"])
def get_visitors():
  return visitors.get_all()

@app.route("/visitors", methods=["POST"])
def add_visitors():
  return visitors.add()

@app.route("/histori_deteksi", methods=["GET"])
def get_histori_deteksi():
  return histori_deteksi.get_all()

@app.route("/histori_deteksi_by_user_id/<user_id>", methods=["GET"])
def get_histori_deteksi_by_user_id(user_id):
  return histori_deteksi.get_all_by_user_id(escape(user_id))

@app.route("/histori_deteksi_by_id_user_dan_kebun/<id_user>/<id_kebun>", methods=["GET"])
def get_all_by_id_user_dan_kebun(id_user, id_kebun):
  return histori_deteksi.get_all_by_id_user_dan_kebun(escape(id_user), escape(id_kebun))

@app.route("/histori_deteksi_by_bulan", methods=["GET"])
def get_histori_deteksi_by_bulan():
  return histori_deteksi.get_by_bulan()

@app.route("/histori_deteksi_terbaru_by_user_id/<user_id>", methods=["GET"])
def get_histori_deteksi_terbaru_by_user_id(user_id):
  return histori_deteksi.get_terbaru_by_user_id(escape(user_id))

@app.route("/histori_deteksi_kebun_by_user_id/<user_id>", methods=["GET"])
def get_histori_deteksi_kebun_by_user_id(user_id):
  return histori_deteksi.get_perkembangan_kebun_by_user_id(escape(user_id))

@app.route("/histori_deteksi", methods=["POST"])
def add_histori_deteksi():
  return histori_deteksi.add()

@app.route("/histori_deteksi", methods=["DELETE"])
def delete_histori_deteksi():
  return histori_deteksi.delete()

# kebun
@app.route("/kebun", methods=["GET"])
def get_kebun():
  return kebun.get_all()

@app.route("/kebun_by_user_id/<user_id>", methods=["GET"])
def get_kebun_by_user_id(user_id):
  return kebun.get_all_by_user_id(escape(user_id))

@app.route("/kebun/<id>", methods=["GET"])
def get_kebun_by_id(id):
  return kebun.get_one(escape(id))

@app.route("/kebun", methods=["POST"])
def add_kebun():
  return kebun.add()

@app.route("/kebun", methods=["PUT"])
def update_kebun():
  return kebun.update()

@app.route("/kebun/<id>", methods=["DELETE"])
def delete_kebun(id):
  return kebun.delete(escape(id))
  
if __name__ == '__main__':
    socketio.run(app, debug=True, host="127.0.0.1")
