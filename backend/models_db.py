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
    lotacao1 = db.Column(db.Integer, nullable=False, default = 0)
    lotacao2 = db.Column(db.Integer, nullable=False, default = 0)
    

    #Representação em String
    def __repr__(self):
        return f"ID: '{self.id_sala}', Nome: '{self.nome}', Lotação e1: '{self.lotacao1}', Lotação e2: '{self.lotacao2}'"

    #Expressão da classe em Json - conversão para Frontend
    def json(self):
        return{
            "id_sala": self.id_sala, "nome": self.nome,
            "lotacao1": self.lotacao1, "lotacao2" : self.lotacao2
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
    sala1_id = db.Column(db.Integer, db.ForeignKey(Sala.id_sala), nullable = True,)
    sala1 = db.relationship("Sala", foreign_keys=sala1_id)
    
    #Chave estrangeira da segunda sala
    sala2_id = db.Column(db.Integer, db.ForeignKey(Sala.id_sala), nullable = True)
    sala2 = db.relationship("Sala", foreign_keys=sala2_id)
    
    #Chave estrangeira do primeiro espaço de café
    cafe1_id = db.Column(db.Integer, db.ForeignKey(Espaco_Cafe.id_espaco), nullable = True)
    cafe1 = db.relationship("Espaco_Cafe", foreign_keys=cafe1_id)
    
    #Chave estrangeira do segundo espaço de café
    cafe2_id = db.Column(db.Integer, db.ForeignKey(Espaco_Cafe.id_espaco), nullable = True)
    cafe2 = db.relationship("Espaco_Cafe", foreign_keys=cafe2_id)
    

    #Representação em String
    def __str__(self):
        return f"Nome: '{self.nome}', Sobrenome: '{self.sobrenome}', Sala1: '{self.sala1_id}, Sala2: '{self.sala2_id}, Cafe1: '{self.cafe1_id}, Cafe2: '{self.cafe2_id} '"

    #Expressão da classe em Json - conversão para Frontend
    def json(self):
        return{
            "cpf": self.cpf, "nome": self.nome,
            "sobrenome": self.sobrenome,
            "cafe1": self.cafe1.json(),
            "cafe2": self.cafe2.json(),
            "sala1": self.sala1.json(),
            "sala2": self.sala2.json(),
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
    s3 = Sala(
        nome = "Sala 3"
    )
    s4 = Sala(
        nome = "Sala 4"
    )
    
    db.session.add(s1)
    db.session.add(s2)
    #db.session.add(s3)
    db.session.commit()
    print(c1)
    print(c2)
    
    print(s1)
    print(s2)
    
    #Gerador de CPF em: https://www.geradorcpf.com/
    p1 = Pessoa(
        cpf = "05435950643",
        nome = "Jonas",
        sobrenome = "Silveira"

    )
    
    p2 = Pessoa(
        cpf = "61284732533",
        nome = "Carlinhos",
        sobrenome = "Teixeira"
    )
    
    p3 = Pessoa(
        cpf = "18187443090",
        nome = "Zéca",
        sobrenome = "Pagodinho"
    )
    
    p4 = Pessoa(
        cpf = "61784818887",
        nome = "Lucas",
        sobrenome = "Machado"
    )
    
    p5 = Pessoa(
        cpf = "88345372546",
        nome = "Anna",
        sobrenome = "Kretz"
    )
    
    p6 = Pessoa(
        cpf = "55564351460",
        nome = "Jarbas",
        sobrenome = "Souza"
    )
    
    p7 = Pessoa(
        cpf = "63414167506",
        nome = "Tobias",
        sobrenome = "Afreim"
    )
        
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.add(p6)
    db.session.add(p7)
    db.session.commit()
    print(p1)
    print(p2)
    
    
    
    

    
   

    
