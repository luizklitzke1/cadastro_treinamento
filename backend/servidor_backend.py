from config import app
from routes import *

#Execute esse módulo para iniciar o servidor backend - por padrão no localhost
if __name__ == '__main__':
    app.run(debug=True)

