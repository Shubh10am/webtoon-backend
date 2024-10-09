import mongoengine
from flask import g
from flask import Flask

from flask_cors import CORS


class BaseConfig(object):
    DEBUG = True
    JWT_IDENTITY_CLAIM = 'identity'
    JWT_TOKEN_LOCATION = ('headers',)
    JWT_COOKIE_CSRF_PROTECT = False
    MONGODB_SETTINGS = {
        "db": "webtoons_db",
        "host": "localhost",
        "port": 27017,
        "connect": False
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'test'
    JWT_SECRET_KEY = 'test'


def init_app():
    config = DevelopmentConfig

    app.config.from_object(config)
    mongoengine.connect(**app.config["MONGODB_SETTINGS"])

    return app


def after_function(flask_app):
    @flask_app.after_request
    def add_header(response):
        response.headers['X-Client-Email'] = getattr(g, 'client_email', "")
        return response


app = Flask(__name__)
init_app()
after_function(app)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173"]}},
            methods=["GET", "POST", "PUT", "DELETE"], supports_credentials=True)
