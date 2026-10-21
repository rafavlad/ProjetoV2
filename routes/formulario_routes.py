from flask import Blueprint, request, jsonify  # Importando as funções necessárias do Flask para criar rotas e manipular requisições.
from flask_jwt_extended import jwt_required, get_jwt_identity  # Importando funcionalidades para trabalhar com JWT.
from controllers.formulario_controller import FormularioController  # Importando o controlador de formulários para processar a lógica de negócios.

# Criando um Blueprint para as rotas de formulários.
formulario_bp = Blueprint('formularios', __name__)

# Rota para criar um novo formulário. Só aceita requisições POST.
# A rota exige um token JWT válido.
@formulario_bp.route('/', methods=['POST'])
@jwt_required()  # Protege a rota, exigindo que o usuário esteja autenticado.
def create_formulario():
    # Obtém o ID do usuário a partir do token JWT.
    user_id = int(get_jwt_identity())
    # Chama o método de criação de formulário no controlador e retorna a resposta em formato JSON.
    body, status = FormularioController.create_formulario(user_id, request.get_json())
    return jsonify(body), status

# Rota para obter todos os formulários do usuário autenticado. Só aceita requisições GET.
# A rota exige um token JWT válido.
@formulario_bp.route('/', methods=['GET'])
@jwt_required()  # Protege a rota, exigindo que o usuário esteja autenticado.
def get_formulario():
    # Obtém o ID do usuário a partir do token JWT.
    user_id = int(get_jwt_identity())
    # Chama o método para obter os formulários do usuário no controlador e retorna a resposta em formato JSON.
    body, status = FormularioController.get_formulario(user_id)
    return jsonify(body), status

# Rota para atualizar um formulário específico. Só aceita requisições PUT.
# A rota exige um token JWT válido.
@formulario_bp.route('/<int:formulario_id>', methods=['PUT'])
@jwt_required()  # Protege a rota, exigindo que o usuário esteja autenticado.
def update_formulario(formulario_id):
    # Obtém o ID do usuário a partir do token JWT.
    user_id = int(get_jwt_identity())
    # Chama o método para atualizar o formulário no controlador e retorna a resposta em formato JSON.
    body, status = FormularioController.update_formulario(user_id, formulario_id, request.get_json())
    return jsonify(body), status

# Rota para excluir um formulário específico. Só aceita requisições DELETE.
# A rota exige um token JWT válido.
@formulario_bp.route('/<int:formulario_id>', methods=['DELETE'])
@jwt_required()  # Protege a rota, exigindo que o usuário esteja autenticado.
def delete_formulario(formulario_id):
    # Obtém o ID do usuário a partir do token JWT.
    user_id = int(get_jwt_identity())
    # Chama o método para excluir o formulário no controlador e retorna a resposta em formato JSON.
    body, status = FormularioController.delete_formulario(user_id, formulario_id)
    return jsonify(body), status
