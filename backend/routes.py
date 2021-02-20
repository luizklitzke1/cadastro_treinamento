#Módulo responsável pra lógica de rotas do servidor backend

from models_db import Pessoa, Sala, Espaco_Cafe
from PIL import Image
import base64
from config import *
import os, io


# Rota para a home
@app.route("/")
def inicio_backend():
    return """
            Escolha uma opção para obter os dados em Json<br>
            <a href='/listar_pessoas'>Listar pessoas </a><br>
            <a href='/listar_salas'>Listar salas</a><br>
            <a href='/listar_espacos_cafe'>Listar espaços para café</a>
            """
            
# Rota para listar as pessoas
@app.route("/listar_pessoas")
def listar_pessoas():
   
    pessoas = db.session.query(Pessoa).all()
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))

# Rota para listar as salas
@app.route("/listar_salas")
def listar_salas():
   
    salas = db.session.query(Sala).all()
    salas_json = [Sala.json() for Sala in salas]
    return (jsonify(salas_json))


# Rota para listar os espaços para café
@app.route("/listar_espacos_cafe")
def listar_espacos_cafe():
   
    espacos_cafe = db.session.query(Espaco_Cafe).all()
    espacos_cafe_json = [Espaco_Cafe.json() for Espaco_Cafe in espacos_cafe]
    return (jsonify(espacos_cafe_json))


# Rota para listar oas pessoas de determinada sala e etapa
@app.route("/listar_pessoas_esp/<int:id_sala>/<int:etapa>",  methods=['POST', 'GET'])
def listar_pessoas_esp(id_sala,etapa):
   
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.sala1_id == id_sala).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.sala2_id == id_sala).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))