
from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(test_config=None):
    
    app = Flask(__name__,instance_relative_config=True)
    
    if test_config is None:
        app.config.from_object(DevelopConfig)
    else:
        app.config.from_mapping(test_config)

    CORS(app)
    db.init_app(app)
    
    with app.app_context():
        # Include routes
        from . import routes 
        return app
   

class Config(object):
    
    DEBUG = False
    TESTING = False
    #Configurações do DB
    
    path = os.path.dirname(os.path.abspath(__file__))
    arquivodb = os.path.join(path, 'dados.db')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + arquivodb
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Remover warnings
    SESSION_COOKIE_SECURE = True
    
class ProductionConfig(Config):
    SESSION_COOKIE_SECURE = True
    pass


class DevelopConfig(Config):
    SESSION_COOKIE_SECURE = False
    DEBUG = True

class TestingConfig(Config):
    
    #Configurações do DB
    path = os.path.dirname(os.path.abspath(__file__))
    arquivodb = os.path.join(path, 'testes.db')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + arquivodb
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Remover warnings
    

    TESTING = True
    SESSION_COOKIE_SECURE = False