from flaskblog import create_app
from flask_socketio import send
from flask_cors import cross_origin
app, manager, socketio = create_app()


@socketio.on("message")
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg + " Tomerrr", broadcast=True)

@socketio.on("message2")
def handle_message2(msg):
    print(f"Message: {msg}")
    send(msg + " Tomerrrxz`xz`xz`xz`", broadcast=True)



if __name__ == '__main__':
    socketio.run(app)
#    app.run(debug=True)

#    manager.run()
