import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config_Class=Config):
    app = Flask(__name__)
    app.config.from_object(config_Class)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    from flaskblog.users.routes import users
    from flaskblog.main.routes import main
    from flaskblog.rooms.routes import rooms
    app.register_blueprint(main)
    app.register_blueprint(rooms)
    app.register_blueprint(users)
    return app

    