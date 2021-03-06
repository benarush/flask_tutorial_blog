from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_caching import Cache


db = SQLAlchemy()
bcrypt = Bcrypt()
socketio = SocketIO(cors_allowed_origins='*')
cors = CORS()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

migrate = Migrate()
manager = Manager()

jwt = JWTManager()

admin = Admin()

cache = Cache()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    cors.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    manager.__init__(app)
    manager.add_command('db', MigrateCommand)
    cache.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.models import User, Post
    from flaskblog.chat.routes import chat
    
    app.register_blueprint(chat)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)


    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(User, db.session))

    manager.add_command('db', MigrateCommand)
    socketio.init_app(app)

    return app, manager, socketio