#Módulo responsável pra lógica de rotas do servidor backend e comunicação com o DB
import json
import os

from flask import jsonify, request, Blueprint
from .models_db import Espaco_Cafe, Pessoa, Sala, db
from flask import current_app as app


geral = Blueprint('geral', __name__)

# Rota para a home
@geral.route("/")
def inicio_backend():
    return """
            Escolha uma opção para obter os dados em Json<br>
            <a href='/listar_pessoas'>Listar pessoas </a><br>
            <a href='/listar_salas'>Listar salas</a><br>
            <a href='/listar_espacos_cafe'>Listar espaços para café</a>
            """
            
# Rota para listar as pessoas
@geral.route("/listar_pessoas")
def listar_pessoas():
   
    pessoas = db.session.query(Pessoa).all()
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))


# Rota para cadastrar pessoas
@geral.route("/cadastrar_pessoa", methods=['POST'])
def cadastar_Pessoa():
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    try: #Tenta fazer o registro
        
        if len(dados["cpf"]) != 11:
            dados["cpf"] = "0" + dados["cpf"]
            
        if not(testar_cpf(dados["cpf"])):
            raise Exception("CPF inválido!")
        
        nova_Pessoa = Pessoa(**dados)
        
        db.session.add(nova_Pessoa)
        alocar_pessoa_sala(nova_Pessoa.sala1_id,nova_Pessoa.cpf,1)
        designar_sala_etapa2(nova_Pessoa)
        alocar_pessoa_cafe(nova_Pessoa.cafe1_id,nova_Pessoa.cpf,1)
        alocar_pessoa_cafe(nova_Pessoa.cafe2_id,nova_Pessoa.cpf,2)

        db.session.commit()
        
        
    #Retorna erro com detalhes
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta

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
    
    alocada = False
    for cafe in espacos_cafe:
        
        if not(alocada):
            if (cafe.id_espaco != pessoa.cafe1_id):
                pessoa.cafe2_id = cafe.id_espaco
                cafe.lotacao2 += 1
                alocada = True
                break
    
    db.session.commit()
            
    
#Rota para designar automaticamente a sala da segunda etapa para uma pessoa
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
            #Garante que 50% sejam mantido e da preferência pra misturar os pessoas

            if ((coincidem < metade or metade == 0) and pessoa.sala1_id == sala.id_sala) or ((coincidem >= metade and pessoa.sala1_id != sala.id_sala)):
                
                for s2 in salas:
                    
                    if (sala.lotacao2 > s2.lotacao2):
                        elegivel = False
                    
                if elegivel:
                    pessoa.sala2_id = sala.id_sala
                    sala.lotacao2 += 1
                    return True
        pessoa.sala2_id = sala1.id_sala



# Rota para  alocar uma pessoa em uma sala
@geral.route("/alocar_pessoa_sala/<int:id_sala>/<string:cpf>/<int:etapa>", methods=['POST'])
def alocar_pessoa_sala(id_sala, cpf, etapa):
    
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
                coincidem = calcular_coincidentes_e_metade(sala.id_sala)[0]
                if coincidem != sala_esp.lotacao1//2:
                    return False
                
        pessoa = Pessoa.query.get_or_404(cpf)
        
        if etapa == 1:
            pessoa.sala1_id = sala_esp.id_sala
            sala_esp.lotacao1 += 1
            #Designa automaticamente um sala pra segunda etapa
        
        elif etapa == 2 and (pessoa.sala2_id != sala_esp.id_sala):
            pessoa.sala2_id = sala_esp.id_sala

            sala_esp.lotacao2 += 1
        
        db.session.commit()
            
        
    #Retorna erro com detalhes
    except: 
        return False
    return True
    
#Alocar pessoa para um espaço de café
@geral.route("/alocar_pessoa_cafe/<int:id_espaco_cafe>/<string:cpf>/<int:etapa>", methods=['POST'])
def alocar_pessoa_cafe(id_espaco_cafe, cpf, etapa, auto = False):
    
    try:
        
        cafe_esp = Espaco_Cafe.query.get_or_404(id_espaco_cafe)
    
        pessoa = Pessoa.query.get_or_404(cpf)
        
        if etapa == 1:
            pessoa.cafe1_id = id_espaco_cafe
            cafe_esp.lotacao1 += 1
            if auto:
                designar_cafe_etapa2(pessoa)
        
        #Evita a repetição do espaço de café
        elif etapa ==2:
            if pessoa.cafe1_id != id_espaco_cafe:
                pessoa.cafe2_id = id_espaco_cafe
                cafe_esp.lotacao2 += 1
            else:
                return False
        
        else:
            return False
       
    except:
        return False
    
    db.session.commit()
    return True


#Realocar todas as pessoas, priorizando suas posições atuais na primeira etapa
def redistribuir_pessoas():
    
    pessoas = db.session.query(Pessoa).all()
    cafes = db.session.query(Espaco_Cafe).all()
    salas = db.session.query(Sala).all()
    
    #Zera a lotação de todas as salas
    for sala in salas:
        sala.lotacao1 = 0
        sala.lotacao2 = 0
        
    for cafe in cafes:
        cafe.lotacao1 = 0
        cafe.lotacao2 = 0

    for pessoa in pessoas:
        
        pessoa.sala1_id = None
        pessoa.sala2_id = None
      
        alocada = False
        #Caso de errado, tenta a proxima elegivel
        for sala in salas:
            if not(alocada):
                if (alocar_pessoa_sala(sala.id_sala,pessoa.cpf,1)):
                    alocada = True
                    continue
        
        
        #Distribui as pessoas nos espaços de café de maneira que não fiquem muito polarizadas também
        #Do contrário, supondo que temos 3 espaços, poderiamos ter 1 com todas pessoas na primeira etapa e outro com todos na
        indexpessoa = pessoas.index(pessoa)
        alocadacafe = False
        
        for cafe in cafes:
            if not(alocadacafe):
                if ((indexpessoa!=0 and len(cafes)>1) and (pessoas[indexpessoa-1].cafe1_id != cafe.id_espaco)):  
                    if (alocar_pessoa_cafe(cafe.id_espaco,pessoa.cpf,1)):
                        alocadacafe = True
                        continue
                    
        alocadacafe2 = False
       
        for cafe in cafes:
            if not(alocadacafe2):
                if (alocar_pessoa_cafe(cafe.id_espaco,pessoa.cpf,2)):
                    alocadacafe2 = True
                    continue
                    
        designar_sala_etapa2(pessoa)
                    
    recalcular_lotacao_salas()
                    
        
                   
# Procurar uma pessoa
@geral.route("/procurar_pessoa", methods=['POST'])
def procurar_pessoa():
    
    dados = request.get_json()
    cpf = dados['cpf']
    nome = dados['nome']
    sobrenome = dados['sobrenome']
    
    pessoas = db.session.query(Pessoa).filter(Pessoa.cpf.like(f"%{cpf}%"),
                                              Pessoa.nome.like(f"%{nome}%"),
                                              Pessoa.sobrenome.like(f"%{sobrenome}%")
                                              ).all()
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
  
    return (jsonify(pessoas_json))

# Rota para pegar os dados de uma pessoa específica
@geral.route("/dados_pessoa/<string:cpf>",  methods=['POST','GET'])
def dados_pessoa(cpf):
    
    if len(cpf) != 11:
        cpf = "0" + cpf
        
    pessoa = Pessoa.query.get_or_404(cpf)
    
    return (pessoa.json())

# Procurar uma pessoa em uma sala específica
@geral.route("/procurar_pessoa_sala/<int:id_sala>/<int:etapa>", methods=['POST'])
def procurar_pessoa_sala(id_sala,etapa):
    
    dados = request.get_json()
    cpf = dados['cpf']
    nome = dados['nome']
    sobrenome = dados['sobrenome']
    
    if etapa == 1 :
        pessoas = db.session.query(Pessoa).filter(Pessoa.cpf.like(f"%{cpf}%"),
                                                Pessoa.nome.like(f"%{nome}%"),
                                                Pessoa.sobrenome.like(f"%{sobrenome}%"),
                                                Pessoa.sala1_id==id_sala
                                                ).all()
    else:
        pessoas = db.session.query(Pessoa).filter(Pessoa.cpf.like(f"%{cpf}%"),
                                                Pessoa.nome.like(f"%{nome}%"),
                                                Pessoa.sobrenome.like(f"%{sobrenome}%"),
                                                Pessoa.sala2_id==id_sala
                                                ).all()
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
  
    return (jsonify(pessoas_json))


# Procurar uma pessoa em um espaço para café específico
@geral.route("/procurar_pessoa_cafe/<int:id_cafe>/<int:etapa>", methods=['POST'])
def procurar_pessoa_cafe(id_cafe,etapa):
    
    dados = request.get_json()
    cpf = dados['cpf']
    nome = dados['nome']
    sobrenome = dados['sobrenome']
    
    if etapa == 1 :
        pessoas = db.session.query(Pessoa).filter(Pessoa.cpf.like(f"%{cpf}%"),
                                                Pessoa.nome.like(f"%{nome}%"),
                                                Pessoa.sobrenome.like(f"%{sobrenome}%"),
                                                Pessoa.cafe1_id==id_cafe
                                                ).all()
    else:
        pessoas = db.session.query(Pessoa).filter(Pessoa.cpf.like(f"%{cpf}%"),
                                                Pessoa.nome.like(f"%{nome}%"),
                                                Pessoa.sobrenome.like(f"%{sobrenome}%"),
                                                Pessoa.cafe2_id==id_cafe
                                                ).all()
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
  
    return (jsonify(pessoas_json))


# Rota para listar oas pessoas de determinado espaço de café e etapa
@geral.route("/listar_pessoas_cafe/<int:id_espaco>/<int:etapa>",  methods=['POST'])
def listar_pessoas_cafe(id_espaco,etapa):
   
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.cafe1_id == id_espaco).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.cafe2_id == id_espaco).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))

# Rota para editar uma Pessoa
@geral.route("/editar_pessoa/<string:cpf>",  methods=['POST'])
def editar_Pessoa(cpf):
   
    dados = request.get_json()
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    if len(cpf) != 11:
        cpf = "0" + cpf
    
    if len(dados["novo_cpf"]) != 11:
        dados["novo_cpf"] = "0" + dados["novo_cpf"] 
        
    if not(testar_cpf(cpf)):
        raise Exception("CPF inválido!")
    
    try:
        pessoa = Pessoa.query.get_or_404(cpf)
        
        pessoa.cpf = dados["novo_cpf"]                                 
        pessoa.nome = dados["novo_nome"]
        pessoa.sobrenome = dados["novo_sobrenome"]
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta


# Rota para apagar uma Pessoa
@geral.route("/apagar_pessoa/<string:cpf>",  methods=['DELETE','POST'])
def apagar_Pessoa(cpf):
    
    if len(cpf) != 11:
        cpf = "0" + cpf
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: #Tentar realizar a exclusão
        pessoa = Pessoa.query.get(cpf)
                                             
        db.session.delete(pessoa)
        redistribuir_pessoas()
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

# Rota para pegar a lista de pessoas de uma sala em uma etapa
@geral.route("/pessoas_sala/<int:id_sala>/<int:etapa>",  methods=['POST','GET'])
def pessoas_sala(id_sala,etapa):
    
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.sala1_id == id_sala).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.sala2_id == id_sala).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))


# Rota para listar as salas
@geral.route("/listar_salas")
def listar_salas():
   
    salas = db.session.query(Sala).all()
    salas_json = [Sala.json() for Sala in salas]
    return (jsonify(salas_json))


# Rota para pegar os dados de uma sala específica
@geral.route("/dados_sala/<int:id_sala>",  methods=['POST','GET'])
def dados_sala(id_sala):
    
    sala_esp = Sala.query.get_or_404(id_sala)
    
    return (sala_esp.json())

# Procurar sala
@geral.route("/procurar_sala", methods=['POST'])
def procurar_sala():
    
    dados = request.get_json()
    nome = dados['nome']
    salas = db.session.query(Sala).filter(Sala.nome.like(f"%{nome}%")).all()
    salas_json = [Sala.json() for Sala in salas]
  
    return (jsonify(salas_json))

# Rota para cadastrar salas
@geral.route("/cadastrar_sala", methods=['POST',])
def cadastrar_sala():
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    
    try: #Tenta fazer o registro
        
        nova_Sala = Sala(**dados)
        db.session.add(nova_Sala)
        redistribuir_pessoas()
        db.session.commit()
        
    #Retorna erro com detalhes
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta

# Rota para apagar uma Sala
@geral.route("/apagar_sala/<int:id_sala>",  methods=['DELETE','POST'])
def apagar_Sala(id_sala):
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: #Tentar realizar a exclusão
        sala = Sala.query.get_or_404(id_sala)
                                               
        db.session.delete(sala)
        redistribuir_pessoas()
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta


# Rota para editar uma Sala
@geral.route("/editar_sala/<int:id_sala>",  methods=['POST'])
def editar_Sala(id_sala):
    
    dados = request.get_json()
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: 
        sala = Sala.query.get_or_404(id_sala)
                                               
        sala.nome = dados["novo_nome"]
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

# Rota para pegar a lista de salas disponíveis na primeira etapa
@geral.route("/listar_sala1_disponiveis",  methods=['GET'])
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
        




# Rota para pegar os dados de um espaço para café 
@geral.route("/dados_cafe/<int:id_espaco>",  methods=['POST','GET'])
def dados_cafe(id_espaco):
    
    cafe_esp = Espaco_Cafe.query.get_or_404(id_espaco)
    
    return (cafe_esp.json())


# Rota para pegar a lista de pessoas de um espaço para café em uma etapa
@geral.route("/pessoas_cafe/<int:id_espaco>/<int:etapa>",  methods=['POST','GET'])
def pessoas_cafe(id_espaco,etapa):
    
    if etapa == 1:
        pessoas = Pessoa.query.filter(Pessoa.cafe1_id == id_espaco).all()
    else:
        pessoas = Pessoa.query.filter(Pessoa.cafe2_id == id_espaco).all()
    
    pessoas_json = [Pessoa.json() for Pessoa in pessoas]
    return (jsonify(pessoas_json))

# Rota para listar os espaços para café
@geral.route("/listar_espacos_cafe")
def listar_espacos_cafe():
   
    espacos_cafe = db.session.query(Espaco_Cafe).all()
    espacos_cafe_json = [Espaco_Cafe.json() for Espaco_Cafe in espacos_cafe]
    return (jsonify(espacos_cafe_json))



# Procurar espaço para café
@geral.route("/procurar_cafe", methods=['POST'])
def procurar_cafe():
    
    dados = request.get_json()
    nome = dados['nome']
    espacos = db.session.query(Espaco_Cafe).filter(Espaco_Cafe.nome.like(f"%{nome}%")).all()
    espacos_json = [Espaco_Cafe.json() for Espaco_Cafe in espacos]
  
    return (jsonify(espacos_json))




# Rota para cadastrar espaços para café
@geral.route("/cadastrar_espaco_cafe", methods=['POST'])
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
@geral.route("/apagar_espaco_cafe/<int:id_espaco>",  methods=['DELETE','POST'])
def apagar_Espaco_cafe(id_espaco):
    
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: #Tentar realizar a exclusão
        espaco = Espaco_Cafe.query.get_or_404(id_espaco) 
        db.session.delete(espaco)
        
        redistribuir_pessoas()  
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta



# Rota para editar um Espaço para café
@geral.route("/editar_cafe/<int:id_cafe>",  methods=['POST'])
def editar_Cafe(id_cafe):
    
    dados = request.get_json()
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    
    try: 
        cafe = Espaco_Cafe.query.get_or_404(id_cafe)
                                               
        cafe.nome = dados["novo_nome"]
        db.session.commit()
        
    except Exception as e:  #Envie mensagem em caso de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta



def testar_cpf(cpf):
    
    
    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True  


#Recacalcula a lotação por erros possíveis com salas ímpares
def recalcular_lotacao_salas():
    salas = db.session.query(Sala).all()
    
    for sala in salas:
        pessoas1 = Pessoa.query.filter(Pessoa.sala1_id == sala.id_sala).all()
        pessoas2 = Pessoa.query.filter(Pessoa.sala2_id == sala.id_sala).all()
        sala.lotacao1 = len(pessoas1)
        sala.lotacao2 = len(pessoas2)
        
        
    cafes = db.session.query(Espaco_Cafe).all()
    
    for cafe in cafes:
        pessoas1 = Pessoa.query.filter(Pessoa.cafe1_id == cafe.id_espaco).all()
        pessoas2 = Pessoa.query.filter(Pessoa.cafe2_id == cafe.id_espaco).all()
        cafe.lotacao1 = len(pessoas1)
        cafe.lotacao2 = len(pessoas2)
        