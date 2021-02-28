#Testa o index geral
def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200


#Um index inexistente
def test_error(app, client):
    res = client.get('/carlos')
    assert res.status_code == 200
