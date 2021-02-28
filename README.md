# Cadastro para Treinamento
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-js](https://img.shields.io/badge/Made%20with-JavaScript-1f425f.svg)](https://www.javascript.com/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) 

📜 Descrição do projeto

O projeto possibilita o cadastro de pessoas, salas e espaços para café de um evento, seguindo alguns requisitos como lógica de organização e fazendo sua manutenção de maneira automática. Veja mais sobre esses requisitos e lógicas abaixo:

A lógica do projeto roda prioritariamente em Python, com requerimentos de dados pela parte gráfica, a qual optei por desenvolver em um ambiente WEB com JavaScript e jQuery, uma vez que me sinto mais confortável e não tenho experiência com *frameworks* de criação de telas para aplicações em Java.

## 👾 Live demo
O sistema está hospedado temporariamente em um servidor gratuito do PyAnywhere, com velocidade limitada, principalmenten nos cadastros, porém funciona bem para visualizar o geral.
Para acessá-lo, [clique nesse link](http://luizklitzke1.pythonanywhere.com/html/html/index.html).

## 🛠 Instalação
  
Para rodar o servidor backend, basta instalar os pacotes necessário, todos listados no arquivo requirements.txt.
O mesmo pode ser feito com pip em um terminal na pasta fonte do projeto através do comando :

```sh
python -m pip install -r backend/requirements.txt
```

Para acessar os dados pelo frontend, basta executar qualquer um dos arquivos .html presentes em ˋfrontend/html/ˋ, **cerifique-se que o servidor backend está rodando para obter os dados!**.

## 💻 Utilização

Para inicilizar o servidor backend, basta inicilizar o módulo servidor_backend.py e o servidor irá rodar por padrão no *localhost*.

O acesso do usuário é feito pelo ambiente web ao se executar os arquivos .html, vide explicação anterior.
Uma vez no site, pode-se navegar tanto pelos links na tela como pela barra de acesso rápido na lateral esquerda.

> O Site funciona de maneira responsiva, logo, se adapta ao tamanho da tela e acessos em dispositivos mobile.
![Responsivo](imgs/respons.gif)

### 🔍Consulta de dados
Em vários locais no sistema, você pode informar os dados desejados para consultar dados de pessoas, salas ou espaços de café em tempo real.
![Responsivo](imgs/search.gif)

## 📈 Lógica de distribuição


### 🚪Salas
O sistema segue uma lógica para a distruibuição de pessoas nas salas:
  * A diferença de pessoas não pode ser maior que um
  * Metade das pessoas devem trocar de sala na segunda etapa
  > 💡 No caso da sala possuir um número impar de pessoas na primeira etapa, a metade é aredondada para baixo. Exemplo: metade de 3 pessoas = ~~1.5~~ 1
  
### ☕Espaços para café
  * A pessoa deve trocar de espaço para café entre o primeiro e segundo intervalo
  > 💡 O sistema de distribuição automática tenta evitar a polarização nesses espaços
  
Logo, um algoritmo garante que tais parâmetros sejam respeitados, organizando automaticamente as pessoas. 
Exemplo da parte principal do código responsável por realocar as pessoas nas salas e espaços para café:
~~~python

        alocada = False
        #Caso de errado, tenta a proxima elegivel
        for sala in salas:
            if not(alocada):
                if (alocar_pessoa_sala(sala.id_sala,pessoa.cpf,1)):
                    alocada = True
                    continue
        
        
        #Distribui as pessoas nos espaços de café de maneira que não fiquem muito polarizadas também
        #Do contrário, supondo que temos 3 espaços, poderiamos ter 1 com todas pessoas na primeira etapa e outro com todos na segunda
        indexpessoa = pessoas.index(pessoa)
        alocadacafe = False
        
        for cafe in cafes:
            if not(alocadacafe):
                if ((indexpessoa!=0 and len(cafes)>1) and (pessoas[indexpessoa-1].cafe1_id != cafe.id_espaco)):  
                    if (alocar_pessoa_cafe(cafe.id_espaco,pessoa.cpf,1)):
                        alocadacafe = True
                        continue
                    
        alocadacafe2 = False
       
        for cafe in cafes:
            if not(alocadacafe2):
                if (alocar_pessoa_cafe(cafe.id_espaco,pessoa.cpf,2)):
                    alocadacafe2 = True
                    continue
                    
        designar_sala_etapa2(pessoa)
                    
    recalcular_lotacao_salas()

~~~
## 🧪 Testes unitários
Os testes unitário são realizados utilizando a biblioteca Pytest em uma instância separada da aplicação e do banco de dados para evitar conflitos com a produção.
Todos os parâmetros para os mesmos são definidos na pasta *tests/*, o que faz também com que para vizualizar os resultados de todos basta digitar **pytest** no prompt de comando, estando na pasta raiz do repositório(uma vez com a biblioteca instalada).
![Testes](imgs/pytest.png)

## 🗃 Persistência de dados

Os dados do programa são armazenados em um banco de dados utilizando a biblioteca SQAlchemy e SQLite e acessados e modificados através de *requests* no back-end.
> Um banco de dados chamado "testes.db" é utilizado apenas durante os testes unitários.

## 🧅 Camadas do projeto

O sistema é dividido em duas partes principais para torná-lo mais modular e seguro, sendo o processamento feito no backend através da utilização de Python e algumas bibliotecas, principalmente Flask, enquanto o frontend é populado pelos dados obtidos do backend através de requisições Ajax pelo jQuery e tem sua lógica de exposição baseada em JavaScript e jQuery.
![Camadas](imgs/estructcamadas.png)




