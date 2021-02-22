#Módulo responsável pra lógica de rotas do servidor backend e comunicação com o DB

from models_db import Pessoa, Sala, Espaco_Cafe
from PIL import Image
import base64
from config import *
import os, io
import json


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

#Rota para designar automaticamente a sala da segunda etapa para uma pessoa
#(A pessoa pode alterar posteriomente, se necessário e atenda os critérios)
def designar_etapa2(pessoa):
    
    salas= db.session.query(Sala).all()
    
    for sala in salas:
        elegivel = True
        pessoas_etapa1 = Pessoa.query.filter_by(sala1_id = sala.id_sala)
        pessoas_etapa2 = Pessoa.query.filter_by(sala2_id = sala.id_sala)
        coincidem =  len([p for p in pessoas_etapa1 if p in pessoas_etapa2 ])
        metade = sala.lotacao1//2
        
        #Garante que 50% sejam mantido e da preferência pra misturar os alunos
        if ((coincidem < metade or metade == 0) and pessoa.sala1_id == sala.id_sala) or ((coincidem >= metade and pessoa.sala1_id != sala.id_sala)):
        
            for s2 in salas:
    
                if (sala.lotacao2 > s2.lotacao2):
                    
                    elegivel = False
                    pass
            if elegivel:
                
                pessoa.sala2_id = sala.id_sala
                sala.lotacao2 += 1
                return True


# Rota para  alocar uma pessoa em uma sala
# http://127.0.0.1:5000/alocar_pessoa_sala/1/05435950643/1
@app.route("/alocar_pessoa_sala/<int:id_sala>/<string:cpf>/<int:etapa>", methods=['POST', 'GET'])
def alocar_pessoa_sala(id_sala, cpf, etapa):
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: #Tenta alocar a pessoa
        
        sala_esp = Sala.query.get_or_404(id_sala)
        
        salas= db.session.query(Sala).all()
        
        for sala in salas:
            
            if etapa == 1:
                
                if (sala_esp.lotacao1 > sala.lotacao1):
                    print("--------","\n",sala_esp.nome,sala.nome)
                    print( sala_esp.lotacao1,sala.lotacao1 )
                    raise Exception("A diferença de pessoas em cada sala deverá ser de no máximo 1 pessoa!")
            else:
                if (sala_esp.lotacao2 > sala.lotacao2):
                    raise Exception("A diferença de pessoas em cada sala deverá ser de no máximo 1 pessoa!")
                
                #Verifica quantas pessoas que tinham essa sala na etapa 1 permaneceram para a etapa, vide a permanencia de 50%
                #Caso seja um número impar, considera o inteiro da divisão por 2
                pessoas_etapa1 = Pessoa.query.filter_by(sala1_id = sala.id_sala)
                pessoas_etapa2 = Pessoa.query.filter_by(sala2_id = sala.id_sala)
                coincidem =  len([p for p in pessoas_etapa1 if p in pessoas_etapa2 ])
                if coincidem != sala_esp.lotacao1//2:
                    raise Exception("Para estimular a troca de conhecimentos, metade das pessoas precisam trocar de sala entre as duas etapas do treinamento.")
                
        
        pessoa = Pessoa.query.get_or_404(cpf)
        
        if etapa == 1 and (pessoa.sala1_id != sala_esp.id_sala):
            pessoa.sala1_id = sala_esp.id_sala
            sala_esp.lotacao1 += 1
            #Designa automaticamente um sala pra segunda etapa
            if not(designar_etapa2(pessoa)):
                raise Exception("aaaaaaaaaaaaaaaaaa")
            
            
        elif etapa == 2 and (pessoa.sala2_id != sala_esp.id_sala):
            pessoa.sala2_id = sala_esp.id_sala
            sala_esp.lotacao2 += 1
        
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