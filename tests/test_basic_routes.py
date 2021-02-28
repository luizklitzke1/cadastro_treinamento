#Testa o index geral
def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200


#Um index inexistente
def test_error(app, client):
    res = client.get('/carlos')
    assert res.status_code == 200
    

#Teste das rotas de listagem
def test_listar_pessoas(app, client):
    res = client.get('/listar_pessoas')
    assert res.status_code == 200

def test_listar_salas(app, client):
    res = client.get('/listar_salas')
    assert res.status_code == 200
    
def test_listar_espacos_cafe(app, client):
    res = client.get('/listar_espacos_cafe')
    assert res.status_code == 200
