from flask import json, jsonify
"""
def test_cadastrar_sala(app,client):
    
    data = {
        'nome': 'sala 111'
    }
    
    response = client.post("/cadastrar_sala", json=data)

    assert response.json['resultado'] == "ok"
"""    

def test_add(app,client):        
    response = client.post(
        '/cadastrar_sala',
        data=json.dumps({'nome': 'sala 313'}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    