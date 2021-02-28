from flask import json, jsonify, request

#Testes básicos para as rotas de CRUD

def test_add_sala(client):        
   response= client.post('/cadastrar_sala', data=json.dumps( {'nome': 'sala 31313'}), content_type='application/json')
   response= client.post('/cadastrar_sala', data=json.dumps( {'nome': 'sala 341'}), content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'ok'
   

def test_editar_sala(client):       
   
   response= client.post('/editar_sala/1',data=json.dumps( {"novo_nome": 'tom'}), content_type='application/json') 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'ok'
   
def test_editar_sala_inexistente(client):       
   
   response= client.post('/editar_sala/23',data=json.dumps( {"novo_nome": 'tom'}), content_type='application/json') 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'erro'
   
def test_apagar_sala(client):       
   
   response= client.post('/cadastrar_sala', data=json.dumps( {'nome': 'sala 23'}), content_type='application/json')
    
   response= client.post('/apagar_sala/3',) 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'ok'
   
   
def test_apagar_sala_inexistente(client):       
   
   response= client.post('/apagar_sala/24',) 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'erro'
   
   
   
   
   
def test_add_espaco_cafe(client):        
   response= client.post('/cadastrar_espaco_cafe', data=json.dumps( {'nome': 'café 123'}), content_type='application/json')
   response= client.post('/cadastrar_espaco_cafe', data=json.dumps( {'nome': 'café 321'}), content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   
   assert data['resultado'] == 'ok'
   

def test_editar_espaco_cafe(client):       
   
   response= client.post('/editar_cafe/1',data=json.dumps( {"novo_nome": 'café 22'}), content_type='application/json') 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'ok'
   
def test_editar_espaco_cafe_inexistente(client):       
   
   response= client.post('/editar_cafe/21',data=json.dumps( {"novo_nome": 'tom'}), content_type='application/json') 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'erro'

def test_apagar_espaco_cafe(client):        
   response= client.post('/cadastrar_espaco_cafe', data=json.dumps( {'nome': 'café 333'}), content_type='application/json')
   response= client.post('/apagar_espaco_cafe/3',) 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'ok'
   
def test_apagar_espaco_cafe_inexistente(client):        
   response= client.post('/apagar_espaco_cafe/99',) 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'erro'
   
   
   

def test_add_pessoa(client):       
   
   dados = {'cpf': '99112585483', 'nome': 'Carlos', 'sobrenome' : 'Silva',
            'sala1_id' : 1, 'cafe1_id': 1, 'cafe2_id': 2,
            }
    
   response= client.post('/cadastrar_pessoa', 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   data = json.loads(response.get_data(as_text=True))

   assert data['detalhes'] == 'ok'

def test_editar_pessoa(client):       
   
   dados = {'novo_cpf': '34602355196', 'novo_nome': 'Augusto', 'novo_sobrenome' : 'Carara',}
    
   response= client.post('/editar_pessoa/99112585483', 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'ok'
   
def test_editar_pessoa_inexistente(client):       
   
   dados = {'novo_cpf': '53847856677', 'novo_nome': 'Augusto', 'novo_sobrenome' : 'Carara',}
    
   response= client.post('/editar_pessoa/53847856677', 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'erro'

def test_apagar_pessoa(client):       
   
   dados = {'cpf': '17715550175', 'nome': 'Geralt', 'sobrenome' : 'Rivia',
            'sala1_id' : 1, 'cafe1_id': 1, 'cafe2_id': 2,
            }
    
   response= client.post('/cadastrar_pessoa', 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   response= client.post('/apagar_pessoa/17715550175',) 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'ok'

def test_apagar_pessoa_inexistente(client):
       
   response= client.post('/apagar_pessoa/9585785757',) 
   data = json.loads(response.get_data(as_text=True))
   assert data['resultado'] == 'erro'
   
def test_add_pessoa_badCPF(client):       
   
   dados = {'cpf': 'awdawdawdawdawd', 'nome': 'Jonas', 'sobrenome' : 'Souza',
            'sala1_id' : 2, 'cafe1_id': 1, 'cafe2_id': 2,
            }
    
   response= client.post('/cadastrar_pessoa', 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   

   assert data['resultado'] == 'erro'
   

def test_add_pessoa_cpf_repetido(client):       
   
   dados = {'cpf': '34602355196', 'nome': 'Jonas', 'sobrenome' : 'Souza',
            'sala1_id' : 2, 'cafe1_id': 1, 'cafe2_id': 2,
            }
    
   response= client.post('/cadastrar_pessoa', 
                         data=json.dumps( dados ), 
                         content_type='application/json')
   data = json.loads(response.get_data(as_text=True))
   
   assert data['resultado'] == 'erro'
   

   
    