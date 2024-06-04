from flask_sqlalchemy import SQLAlchemy


class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = None



class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Stolen.sqlite3'

    SECRET_KEY =  'vish_30'
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = 'vish_30'


db = SQLAlchemy()