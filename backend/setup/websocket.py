from flask_socketio import SocketIO, emit

socketio = SocketIO()

@socketio.on('json')
def handle_message(msg):
    print('Received message: ' + msg)
    emit('json', msg, json=True, broadcast=True)