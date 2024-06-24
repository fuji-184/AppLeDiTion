from flask import Flask
from flask_cors import CORS
from setup.websocket import socketio
from datetime import timedelta

from controller.klasifikasi import klasifikasi_route
from controller.auth import jwt, daftar, masuk, keluar
from controller.pengobatan import obat

from setup.postgresql import db

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "Fast And Focus"
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_TOKEN_LOCATION'] = 'cookies'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
# app.config['JWT_CSRF_CHECK_FORM'] = False
# app.config['JWT_CSRF_IN_COOKIES'] = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_COOKIE_DOMAIN'] = "127.0.0.1"
app.config['JWT_SAME_SITE'] = "Lax"
# app.config['JWT_SESSION_COOKIE'] = False

CORS(app, supports_credentials=True)

socketio.init_app(app, cors_allowed_origins="http://127.0.0.1:5173")
jwt.init_app(app)

@app.route('/')
def home():
    return 'home'

@app.route('/klasifikasi', methods=['POST'])
def klasifikasi():
    return klasifikasi_route()
    
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

if __name__ == '__main__':
    socketio.run(app, debug=True, host="127.0.0.1")
