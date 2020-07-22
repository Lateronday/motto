from app.config.settings import config
from flask import Flask
from app.extension import db
from flask_migrate import Migrate
from app.api.cant_forget import motto


app = Flask(__name__)


def create_app(config_name=None):
    if not config_name:
        config_name = 'development'
    app.config.from_object(config[config_name])
    Migrate(app, db)
    register_db(app)
    register_blueprint(app)
    print(app.url_map)
    return app


def register_db(app):
    db.init_app(app)


def register_blueprint(app):
    app.register_blueprint(motto, url_prefix='/api/motto')
