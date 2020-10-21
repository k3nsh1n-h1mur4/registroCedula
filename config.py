import os



class Config:
    SECRET_KEY = 'isaacabimael'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://k3nsh1n:k0rn82...@localhost/accionFemenil'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
        'development': DevelopmentConfig,
        'default' : DevelopmentConfig
        }
