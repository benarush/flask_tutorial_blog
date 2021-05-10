from flask import Blueprint, render_template
from flask_socketio import send, SocketIO
from flaskblog import socketio

chat = Blueprint('chat', __name__,)

# @socketio.on("messages")
# def message(msg):
#     print(f"Message: {msg}")
#     send(msg, broadcast=True)


@chat.route('/chat')
def chat_view():
    return render_template('chat.html', title='chat')
