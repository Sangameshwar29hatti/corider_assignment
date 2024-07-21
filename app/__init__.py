from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config
from app.main import main as main_blueprint

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(main_blueprint)

    return app
