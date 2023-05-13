import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    """ Base Configuration Class, other classes inherit from this. """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("FLASK_SQLITE_DB") or "sqlite:///" + os.path.join(basedir, "data.sqlite")
    NYT_API_KEY = os.environ.get("NYT_API_KEY") or "your-nyt-api-key"
    RELOAD = os.environ.get("FLASK_RELOAD") or False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    TESTING = False
    DEBUG = os.environ.get("FLASK_DEBUG") or False

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    """ Prod Configuration Class, dev and testing classes inherit from this. """

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(ProductionConfig):
    TESTING=True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "nytwords-test.db")


class DevelopmentConfig(ProductionConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "nytwords-dev.db")


class DockerConfig(ProductionConfig): 
    
    @classmethod
    def init_app(cls, app): 
        ProductionConfig.init_app(app)
        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'docker': DockerConfig,
    
    'default': DevelopmentConfig
}