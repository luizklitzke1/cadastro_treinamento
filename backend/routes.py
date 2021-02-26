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

# Rota para pegar os dados de uma sala específica
@app.route("/dados_sala/<int:id_sala>",  methods=['POST','GET'])
def dados_sala(id_sala):
    
    sala_esp = Sala.query.get_or_404(id_sala)
    
    return (sala_esp.json())


# Rota para pegar a lista de pessoas de uma sala em uma etapa
@app.route("/pessoas_sala/<int:id_sala>/<int:etapa>",  methods=['POST','GET'])
def pessoas_sala(id_sala,etapa):
    
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.sala1_id == id_sala).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.sala2_id == id_sala).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))

# Rota para listar os espaços para café
@app.route("/listar_espacos_cafe")
def listar_espacos_cafe():
   
    espacos_cafe = db.session.query(Espaco_Cafe).all()
    espacos_cafe_json = [Espaco_Cafe.json() for Espaco_Cafe in espacos_cafe]
    return (jsonify(espacos_cafe_json))


# Rota para listar oas pessoas de determinada sala e etapa
@app.route("/listar_pessoas_sala/<int:id_sala>/<int:etapa>",  methods=['POST'])
def listar_pessoas_sala(id_sala,etapa):
   
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.sala1_id == id_sala).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.sala2_id == id_sala).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))

# Rota para listar oas pessoas de determinado espaço de café e etapa
@app.route("/listar_pessoas_cafe/<int:id_espaco>/<int:etapa>",  methods=['POST'])
def listar_pessoas_cafe(id_espaco,etapa):
   
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.cafe1_id == id_espaco).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.cafe2_id == id_espaco).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))


# Rota para cadastrar pessoas
@app.route("/cadastrar_pessoa", methods=['POST'])
def cadastar_Pessoa():
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    try: #Tenta fazer o registro
        
        nova_Pessoa = Pessoa(**dados)
        
        #Testa se foi informada alguma foto para salvar nos arquivos, ou mantém a padrão
        if (dados["foto"] != None):
            nova_Pessoa.foto = salvar_imagem_base64('../front_end/static/imagens_pessoas',(dados["foto"]))
        
        db.session.add(nova_Pessoa)
        alocar_pessoa_sala(nova_Pessoa.sala1_id,nova_Pessoa.cpf,1)
        alocar_pessoa_cafe(nova_Pessoa.cafe1_id,nova_Pessoa.cpf,1)
        
        db.session.commit()
        
        
    #Retorna erro com detalhes
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta

# Rota para cadastrar espaços para café
@app.route("/cadastrar_espaco_cafe", methods=['POST'])
def cadastrar_Espaco_Cafe():
    
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

# Rota para apagar um Espaço para Café
@app.route("/apagar_espaco_cafe/<int:id_espaco_cafe>",  methods=['DELETE'])
def apagar_Espaco_cafe(id_espaco_cafe):
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: #Tentar realizar a exclusão
        espaco = Espaco_Cafe.query.get_or_404(id_espaco_cafe)
                                               
        db.session.delete(espaco)
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

# Rota para cadastrar salas
@app.route("/cadastrar_sala", methods=['POST'])
def cadastrar_sala():
    
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

# Rota para apagar uma Sala
@app.route("/apagar_sala/<int:id_sala>",  methods=['DELETE'])
def apagar_Sala(id_sala):
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: #Tentar realizar a exclusão
        sala = Sala.query.get_or_404(id_sala)
                                               
        db.session.delete(sala)
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

# Rota para apagar uma Pessoa
@app.route("/apagar_pessoa/<string:cpf>",  methods=['DELETE'])
def apagar_Pessoa(cpf):
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: #Tentar realizar a exclusão
        pessoa = Pessoa.query.get_or_404(cpf)
                                               
        db.session.delete(pessoa)
        redistribuir_pessoas()
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

# Rota para pegar a lista de salas disponíveis na primeira etapa
@app.route("/listar_sala1_disponiveis",  methods=['GET'])
def listar_salas1_diposniveis():
    
    salas= db.session.query(Sala).all()
    salas_elegiveis = []
    
    for sala in salas:
        
        elegivel = True
        for s2 in salas:
            if (sala.lotacao1 > s2.lotacao1):
                elegivel = False
                break
        
        if elegivel:
            salas_elegiveis.append(sala.json())
    
    return (jsonify(salas_elegiveis))

def calcular_coincidentes_e_metade(id_sala):
    
    #Pega a lista de pessoas na primeira e segunda etapa e descobre quantas continuaram na segunda
    #E calcula o 50% esperados - aredondando pra baixo em caso de imapr
    sala = Sala.query.get_or_404(id_sala)
    pessoas_etapa1 = Pessoa.query.filter_by(sala1_id = id_sala)
    pessoas_etapa2 = Pessoa.query.filter_by(sala2_id = id_sala)
    coincidem =  len([p for p in pessoas_etapa1 if p in pessoas_etapa2 ])
    metade = sala.lotacao1//2
    return(coincidem, metade)


def designar_cafe_etapa2(pessoa):
    
    espacos_cafe = db.session.query(Espaco_Cafe).all()
    
    for cafe in espacos_cafe:
        if (cafe.id_espaco != pessoa.cafe1_id):
            pessoa.cafe2_id = cafe.id_espaco
            print(cafe)
            cafe.lotacao2 += 1
    
#Rota para designar automaticamente a sala da segunda etapa para uma pessoa
#(A pessoa pode alterar posteriomente, se necessário e atenda os critérios)
def designar_sala_etapa2(pessoa):
    
    salas= db.session.query(Sala).all()
    
    coincidem, metade = calcular_coincidentes_e_metade(pessoa.sala1_id)
    sala1 = Sala.query.get_or_404(pessoa.sala1_id)
    
    #Verifica primeiramente se a sala da pessoa na etapa 1 precisa ter sua porcentagem mantida
    # Feita fora do loop, uma vez que outra sala pode ser elegivel antes dessa
    if ((coincidem < metade or metade == 0) and (pessoa.sala1_id == sala1.id_sala)):
        pessoa.sala2_id = sala1.id_sala
        pessoa.sala1.lotacao2 += 1
        return True
    
    else:
        for sala in salas:
            elegivel = True
            coincidem, metade =  calcular_coincidentes_e_metade(sala.id_sala)
            #Garante que 50% sejam mantido e da preferência pra misturar os alunos
            
            if ((coincidem < metade or metade == 0) and pessoa.sala1_id == sala.id_sala) or ((coincidem >= metade and pessoa.sala1_id != sala.id_sala)):
            
                for s2 in salas:
        
                    if (sala.lotacao2 > s2.lotacao2):
                        
                        elegivel = False
                        pass
                if elegivel:
                    print(sala.id_sala)
                    pessoa.sala2_id = sala.id_sala
                    sala.lotacao2 += 1
                    return True


# Rota para  alocar uma pessoa em uma sala
# http://127.0.0.1:5000/alocar_pessoa_sala/1/05435950643/1
@app.route("/alocar_pessoa_sala/<int:id_sala>/<string:cpf>/<int:etapa>", methods=['POST'])
def alocar_pessoa_sala(id_sala, cpf, etapa):
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: #Tenta alocar a pessoa
        
        sala_esp = Sala.query.get_or_404(id_sala)
        
        salas= db.session.query(Sala).all()
        
        for sala in salas:
            
            if etapa == 1:
                
                if (sala_esp.lotacao1 > sala.lotacao1):
                    return False
            else:
                if (sala_esp.lotacao2 > sala.lotacao2):
                    return False
                
                #Verifica quantas pessoas que tinham essa sala na etapa 1 permaneceram para a etapa, vide a permanencia de 50%
                #Caso seja um número impar, considera o inteiro da divisão por 2
                coincidem = calcular_coincidentes_e_metade(sala.id_sala)[0]
                if coincidem != sala_esp.lotacao1//2:
                    return False
                
        pessoa = Pessoa.query.get_or_404(cpf)
        
        if etapa == 1:
            pessoa.sala1_id = sala_esp.id_sala
            sala_esp.lotacao1 += 1
            #Designa automaticamente um sala pra segunda etapa
            if not(designar_sala_etapa2(pessoa)):
                return False
            
            
        elif etapa == 2 and (pessoa.sala2_id != sala_esp.id_sala):
            pessoa.sala2_id = sala_esp.id_sala
            sala_esp.lotacao2 += 1
        
        db.session.commit()
            
        
    #Retorna erro com detalhes
    except: 
        return False
    
    return True
    
#Alocar pessoa para um espaço de café
@app.route("/alocar_pessoa_cafe/<int:id_espaco_cafe>/<string:cpf>/<int:etapa>", methods=['POST'])
def alocar_pessoa_cafe(id_espaco_cafe, cpf, etapa):
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try:
        
        cafe_esp = Espaco_Cafe.query.get_or_404(id_espaco_cafe)
    
        pessoa = Pessoa.query.get_or_404(cpf)
        
        if etapa == 1:
            pessoa.cafe1_id = id_espaco_cafe
            cafe_esp.lotacao1 += 1
            designar_cafe_etapa2(pessoa)
        
        #Evita a repetição do espaço de café
        elif pessoa.cafe1_id != id_espaco_cafe:
            designar_cafe_etapa2(pessoa)
        
        else:
            raise Exception("O espaço de café não pode se repetir nas duas etapas!")
       
     #Retorna erro com detalhes
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        
    db.session.commit()
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta


#Realocar todas as pessoas, priorizando suas posições atuais na primeira etapa
def redistribuir_pessoas():
    
    pessoas = db.session.query(Pessoa).all()
    salas = db.session.query(Sala).all()
    
    #Zera a lotação de todas as salas
    for sala in salas:
        sala.lotacao1 = 0
        sala.lotacao2 = 0
        
    for pessoa in pessoas:
        
        #Tenta inicialmente alocar a pessoa em sua sala original da primeira etapa
        if not(alocar_pessoa_sala(pessoa.sala1_id,pessoa.cpf,1)):
           
           #Caso de errado, tenta a proxima elegivel
           for sala in salas:
               alocar_pessoa_sala(sala.id_sala,pessoa.cpf,1)
        

#Método para salvar imagens de perfil compactadas
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