from flask import json, jsonify, request

#Testes básicos para as rotas de cadastro

def test_add_sala(app,client):        
   response= client.post("/cadastrar_sala", data=json.dumps( {'nome': 'sala 31313'}), content_type='application/json')
   response= client.post("/cadastrar_sala", data=json.dumps( {'nome': 'sala 341'}), content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   assert data["resultado"] == "ok"
   
def test_add_espaco_cafe(app,client):        
   response= client.post("/cadastrar_espaco_cafe", data=json.dumps( {'nome': 'café 123'}), content_type='application/json')
   response= client.post("/cadastrar_espaco_cafe", data=json.dumps( {'nome': 'café 321'}), content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   
   assert data["resultado"] == "ok"


def test_add_pessoa(app,client):       
   
   dados = {'cpf': "99112585483", 'nome': 'Carlos', 'sobrenome' : "Silva",
            "sala1_id" : 1, "cafe1_id": 1, "cafe2_id": 2,
            }
    
   response= client.post("/cadastrar_pessoa", 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   

   assert data["detalhes"] == "ok"
   
def test_add_pessoa_badCPF(app,client):       
   
   dados = {'cpf': "awdawdawdawdawd", 'nome': 'Jonas', 'sobrenome' : "Souza",
            "sala1_id" : 2, "cafe1_id": 1, "cafe2_id": 2,
            }
    
   response= client.post("/cadastrar_pessoa", 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   

   assert data["resultado"] == "erro"
   

def test_add_pessoa_cpf_repetido(app,client):       
   
   dados = {'cpf': "99112585483", 'nome': 'Jonas', 'sobrenome' : "Souza",
            "sala1_id" : 2, "cafe1_id": 1, "cafe2_id": 2,
            }
    
   response= client.post("/cadastrar_pessoa", 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   
   assert data["resultado"] == "erro"
   

   
    