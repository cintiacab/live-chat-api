from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/live-chat')
def chat_page():  
    return render_template('index.html')

#WebSocket
@socketio.on('connect')
def handle_connect():
    print('Client connected to the server')

@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected from the server')

if __name__ == '__main__':
    socketio.run(app, debug=True)



