from flask_socketio import SocketIO, emit
from setup.postgresql import db

socketio = SocketIO()

@socketio.on('kirim_pesan')
def handle_message(data):
    print('Received message: ' + str(data))
    hasil = db.query(query="insert into chats(id_user, pesan) values(%s, %s) returning id", params=(data['id_user'], data['pesan'],))
    data['id'] = hasil['id']
    emit('pesan_diterima', data, broadcast=True)