from flask import Flask
from flask_cors import CORS
from setup.websocket import socketio

from controller.klasifikasi import klasifikasi_route
from controller.auth import daftar

from setup.postgresql import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "Fast And Focus"
CORS(app)

socketio.init_app(app, cors_allowed_origins="http://localhost:5173")

@app.route('/')
def home():
    return 'home'

@app.route('/klasifikasi', methods=['POST'])
def klasifikasi():
    return klasifikasi_route()
    
@app.route("/daftar", methods=['POST'])
def signup():
  return daftar()

if __name__ == '__main__':
    socketio.run(app, debug=True)
