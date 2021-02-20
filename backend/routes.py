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
@app.route("/listar_pessoas_sala/<int:id_sala>/<int:etapa>",  methods=['POST', 'GET'])
def listar_pessoas_sala(id_sala,etapa):
   
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.sala1_id == id_sala).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.sala2_id == id_sala).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))

# Rota para listar oas pessoas de determinado espaço de café e etapa
@app.route("/listar_pessoas_cafe/<int:id_espaco>/<int:etapa>",  methods=['POST', 'GET'])
def listar_pessoas_cafe(id_espaco,etapa):
   
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.cafe1_id == id_espaco).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.cafe2_id == id_espaco).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))


# Rota para registrar pessoas
@app.route("/registrar_pessoa", methods=['POST'])
def registrar_Pessoa():
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    try: #Tenta fazer o registro
        
        nova_Pessoa = Pessoa(**dados)
        
        #Testa se foi informada alguma foto para salvar nos arquivos, ou mantém a padrão
        if (dados["foto"] != None):
            nova_Pessoa.foto = salvar_imagem_base64('../front_end/static/imagens_pessoas',(dados["foto"]))
        
        db.session.add(nova_Pessoa)
        db.session.commit()
        
    #Retorna erro com detalhes
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta

# Rota para registrar espaços para café
@app.route("/registrar_espaco_cafe", methods=['POST'])
def registrar_Espaco_Cafe():
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    try: #Tenta fazer o registro
        
        novo_Espaco = Espaco_Cafe(**dados)
        
        db.session.add(novo_Espaco)
        db.session.commit()
        
    #Retorna erro com detalhes
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta

# Rota para registrar salas
@app.route("/registrar_sala", methods=['POST'])
def registrar_Sala():
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    
    try: #Tenta fazer o registro
        
        nova_Sala = Sala(**dados)
        
        db.session.add(nova_Sala)
        db.session.commit()
        
    #Retorna erro com detalhes
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta

# Método para salvar imagens de perfil compactadas
def salvar_imagem_base64(diretorio, base64str):
    
    rhex = secrets.token_hex(9)
    nome_foto = rhex + ".png"
    caminho = os.path.join(app.root_path, diretorio, nome_foto)
    tamanho_imagem = (200, 200)
    
    image = base64.b64decode(str(base64str)) 
    
    imagem_menor = Image.open(io.BytesIO(image))
    imagem_menor.thumbnail(tamanho_imagem)
    imagem_menor.save(caminho)
    
    return nome_foto


# Método para apagar as imagens
def apagar_imagem(diretorio, foto):
    
    #Verifica se não é a imagem padrão
    if (foto != "pessoa.png"):
        caminho = os.path.join(app.root_path, diretorio, foto)
        os.remove(caminho)