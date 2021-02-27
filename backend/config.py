
import os
import secrets
from datetime import datetime

from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from PIL import Image

#Criação do APP
app = Flask(__name__)

#Set da conexão do CORS
CORS(app)

path = os.path.dirname(os.path.abspath(__file__))

#Configurações do DB
arquivodb = os.path.join(path, 'dados.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivodb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Remover warnings

db = SQLAlchemy(app)


