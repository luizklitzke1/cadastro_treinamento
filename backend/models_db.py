from config import *

#Classe para os dados de um Espaço de Café
class Espaco_Cafe(db.Model):
    id_espaco = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    
    #Representação em String
    def __repr__(self):
        return f"ID: '{self.id_espaco}', Nome: '{self.nome}'"

    #Expressão da classe em Json - conversão para Frontend
    def json(self):
        return{
            "id_espaco": self.id_espaco, "nome": self.nome,
        }

#Classe para os dados de uma Sala
class Sala(db.Model):
    id_sala = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    #Lotação é modificada toda vez que um aluno entra ou sai, para evitar muitas requisições ao DB
    lotacao = db.Column(db.Integer, nullable=False, default = 0)
    

    #Representação em String
    def __repr__(self):
        return f"ID: '{self.id_sala}', Nome: '{self.nome}', Lotação: '{self.lotacao}'"

    #Expressão da classe em Json - conversão para Frontend
    def json(self):
        return{
            "id_sala": self.id_sala, "nome": self.nome,
            "lotacao": self.lotacao,
        }
      


#Classe para os dados de uma Pessoa
class Pessoa(db.Model):
    
    #Optei por utilizar o CPF como chave primaria para identificação 
    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    sobrenome = db.Column(db.String(150), nullable=False)

    #Endereço em string para o arquivo salvo em Static - gera ao registrar -
    foto = db.Column(db.String(20), nullable=False, default='pessoa.png')
    
    
    #Chave estrangeira da primeira sala
    sala1_id = db.Column(db.Integer, db.ForeignKey(Sala.id_sala), nullable = False)
    sala1 = db.relationship("Sala", foreign_keys=sala1_id)
    
    #Chave estrangeira da segunda sala
    sala2_id = db.Column(db.Integer, db.ForeignKey(Sala.id_sala), nullable = False)
    sala2 = db.relationship("Sala", foreign_keys=sala2_id)
    
    #Chave estrangeira do primeiro espaço de café
    cafe1_id = db.Column(db.Integer, db.ForeignKey(Espaco_Cafe.id_espaco), nullable = False)
    cafe1 = db.relationship("Espaco_Cafe", foreign_keys=cafe1_id)
    
    #Chave estrangeira do segundo espaço de café
    cafe2_id = db.Column(db.Integer, db.ForeignKey(Espaco_Cafe.id_espaco), nullable = False)
    cafe2 = db.relationship("Espaco_Cafe", foreign_keys=cafe2_id)
    

    #Representação em String
    def __str__(self):
        return f"Nome: '{self.nome}', Sobrenome: '{self.sobrenome}', Sala1: '{self.sala1.nome}, Sala2: '{self.sala2.nome}, Cafe1: '{self.cafe1.nome}, Cafe2: '{self.cafe2.nome} '"

    #Expressão da classe em Json - conversão para Frontend
    def json(self):
        return{
            "cpf": self.cpf, "nome": self.nome,
            "sobrenome": self.sobrenome,
            "cafe1": self.cafe1.json(),
            "cafe2": self.cafe2.json(),
            "sala1": self.sala1.json(),
            "sala2": self.sala1.json(),
            "foto": self.foto,
        }
  

#Cria os valores para teste e o arquivo novo, caso executado esse modulo diretamente
if __name__ == "__main__":
    
    #Apaga o DB, se já existir
    
    if os.path.exists(arquivodb):
        os.remove(arquivodb)
        
    db.create_all()
    
    c1 = Espaco_Cafe(
        nome = "Café 1"
    )
    c2 = Espaco_Cafe(
        nome = "Café 2"
    )
    
    db.session.add(c1)
    db.session.add(c2)
    
    s1 = Sala(
        nome = "Sala 1"
    )
    s2 = Sala(
        nome = "Sala 2"
    )
    
    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()
    print(c1)
    print(c2)
    
    print(s1)
    print(s2)
    
    #Gerador de CPF em: https://www.geradorcpf.com/
    p1 = Pessoa(
        cpf = "05435950643",
        nome = "Jonas",
        sobrenome = "Silveira",
        sala1_id = 2,
        sala2_id = 1,
        cafe1_id = 2,
        cafe2_id = 1,
        
    )
    
    p2 = Pessoa(
        cpf = "61284732533",
        nome = "Carlinhos",
        sobrenome = "Teixeira",
        sala1 = s1,
        sala2 = s2,
        cafe1 = c1,
        cafe2 = c2,
        
    )
        
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1)
    print(p2)
    
    
    
    

    
   

    
