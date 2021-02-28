from flask import json, jsonify, request

def test_add(app,client):        
   response= client.post("/cadastrar_sala", data=json.dumps( {'nome': 'sala 31313'}), content_type='application/json')
   assert response.status_code == 200
    