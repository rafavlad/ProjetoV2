from flask import Blueprint, request, jsonify  # Importando as funções necessárias do Flask para criar rotas e manipular requisições.
from flask_jwt_extended import jwt_required, get_jwt_identity  # Importando funcionalidades para trabalhar com JWT.
from controllers.user_controller import UserController  # Importando o controlador de usuários para processar a lógica de negócios.

# Criando um Blueprint para as rotas de usuários.
user_bp = Blueprint('users', __name__)

# Rota para registrar um novo usuário. Só aceita requisições POST.
@user_bp.route('/register', methods=['POST'])
def register():
    # Chama o método de registro de usuário no controlador e retorna a resposta em formato JSON.
    body, status = UserController.register_user(request.get_json())
    return jsonify(body), status

# Rota para fazer login de um usuário. Só aceita requisições POST.
@user_bp.route('/login', methods=['POST'])
def login():
    # Chama o método de login de usuário no controlador e retorna a resposta em formato JSON.
    body, status = UserController.login_user(request.get_json())
    return jsonify(body), status

# Rota para obter informações do usuário autenticado. Só aceita requisições GET.
# A rota exige um token JWT válido.
@user_bp.route('/me', methods=['GET'])
@jwt_required()  # Protege a rota, exigindo que o usuário esteja autenticado.
def get_user():
    # Obtém o ID do usuário a partir do token JWT.
    user_id = int(get_jwt_identity())
    # Chama o método para obter os dados do usuário no controlador e retorna a resposta em formato JSON.
    body, status = UserController.get_user(user_id)
    return jsonify(body), status

# Rota para atualizar as informações do usuário autenticado. Só aceita requisições PUT.
# A rota exige um token JWT válido.
@user_bp.route('/me', methods=['PUT'])
@jwt_required()  # Protege a rota, exigindo que o usuário esteja autenticado.
def update_user():
    # Obtém o ID do usuário a partir do token JWT.
    user_id = int(get_jwt_identity())
    # Chama o método para atualizar os dados do usuário no controlador e retorna a resposta em formato JSON.
    body, status = UserController.update_user(user_id, request.get_json())
    return jsonify(body), status

# Rota para excluir o usuário autenticado. Só aceita requisições DELETE.
# A rota exige um token JWT válido.
@user_bp.route('/me', methods=['DELETE'])
@jwt_required()  # Protege a rota, exigindo que o usuário esteja autenticado.
def delete_user():
    # Obtém o ID do usuário a partir do token JWT.
    user_id = int(get_jwt_identity())
    # Chama o método para excluir o usuário no controlador e retorna a resposta em formato JSON.
    body, status = UserController.delete_user(user_id)
    return jsonify(body), status
