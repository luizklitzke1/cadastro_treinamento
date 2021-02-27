from config import app
from routes import *

import pytest

#Execute esse módulo para iniciar o servidor backend - por padrão no localhost
if __name__ == '__main__':

    app.run(debug=True)
    

def test_conexao_basica():
    
    client = app.test_client()

    res = client.get('/listar_salas')
    
    print(res)
