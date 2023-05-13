from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

import logging

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_class])
    config[config_class].init_app(app)

    app.logger.setLevel(logging.DEBUG)

    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    from .api import bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v0')

    db.init_app(app)
    migrate.init_app(app, db)

    return app

from . import models