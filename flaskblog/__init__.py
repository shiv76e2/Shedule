from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import Config

db = SQLAlchemy()


def create_app(config_Class=Config):
    app = Flask(__name__)
    app.config.from_object(config_Class)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    from flaskblog.main.routes import main
    app.register_blueprint(main)
    return app

    