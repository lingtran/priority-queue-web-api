import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG=False
    TESTING=False
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG=True
    DEVELOPMENT=True
    SESSION_COOKIE_SECURE = False
