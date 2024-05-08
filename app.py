from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import usuario  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/financeiro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

""" def adicionar_usuarios_teste():
    usuarios_teste = [
        {'nome': 'Teste1', 'email': 'teste1@example.com', 'senha': 'senha123'},
        {'nome': 'Teste2', 'email': 'teste2@example.com', 'senha': 'senha456'},
        {'nome': 'Teste3', 'email': 'teste3@example.com', 'senha': 'senha789'}
    ]

    for usuario in usuarios_teste:
        novo_usuario = usuario(nome=usuario['nome'], email=usuario['email'], senha=usuario['senha'])
        db.session.add(novo_usuario)

    db.session.commit()


if __name__ == '__main__':
    adicionar_usuarios_teste() 
    app.run(debug=True) """
