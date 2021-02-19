
from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from PIL import Image

import secrets
import os

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


