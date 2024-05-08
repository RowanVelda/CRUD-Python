from flask import Blueprint, request, jsonify
from app import db
from models import Usuario


usuario_routes = Blueprint('usuario_routes', __name__)

#Post Request
@usuario_routes.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    novo_usuario = Usuario(nome=dados['nome'], email=dados['email'], senha=dados['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário criado com sucesso'}), 201

#Get Requests
@usuario_routes.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.serialize() for usuario in usuarios]), 200

@usuario_routes.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
    return jsonify(usuario.serialize()), 200

#Put Requests
@usuario_routes.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.json
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
    usuario.nome = dados['nome']
    usuario.email = dados['email']
    usuario.senha = dados['senha']
    db.session.commit()
    return jsonify({'mensagem': 'Usuário atualizado com sucesso'}), 200

#Delete Request
@usuario_routes.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário deletado com sucesso'}), 200
