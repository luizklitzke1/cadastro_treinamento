from config import *

#Classe para os dados dos Personagens
class Pessoa(db.Model):
    
    #Optei por utilizar o CPF como chave primaria para identificação 
    cpf = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    sobrenome = db.Column(db.String(150), nullable=False)
   
    data_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #Endereço em string para o arquivo salvo em Static - gera ao registrar -
    foto = db.Column(db.String(20), nullable=False, default='pessoa.png')


    #Representação em String
    def __str__(self):
        return f"Nome: '{self.nome}', Sobrenome: '{self.sobrenome}', Data de Registro: '{self.data_registro}'"

    #Expressão da classe em Json - conversão para Frontend
    def json(self):
        return{
            "cpf": self.cpf, "nome": self.nome,
            "sobrenome": self.sobrenome,
            "data_criacao": self.data_criacao, "foto": self.foto,
        }
        

#Classe para os dados de uma aventura
class Sala(db.Model):
    id_sala = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    lotacao = db.Column(db.Integer, nullable=False)
    
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #Representação em String
    def __repr__(self):
        return f"Nome: '{self.nome}', Lotação: '{self.nome_mestre}', Criação: '{self.data_criacao}'"

    #Expressão da classe em Json - conversão para Frontend
    def json(self):
        return{
            "id_sala": self.id_sala, "nome": self.nome,
            "lotacao": self.lotacao, "data_criacao": self.data_criacao,
        }
        

#Cria os valores para teste e o arquivo novo, caso executado esse modulo diretamente
if __name__ == "__main__":
    
    #Apaga o DB, se já existir
    
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
        
    db.create_all()

    
   

    
