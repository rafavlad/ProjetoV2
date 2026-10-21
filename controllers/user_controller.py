from werkzeug.security import generate_password_hash, check_password_hash  # Importa funções para hash de senha.
from flask_jwt_extended import create_access_token  # Importa função para criar tokens de acesso JWT.
from models.user_model import UserModel  # Importa o modelo de usuário para interagir com o banco de dados.

class UserController:
    # Método estático para registrar um novo usuário.
    @staticmethod
    def register_user(data):
        username = data.get('username')  # Obtém o nome de usuário dos dados fornecidos.
        password = data.get('password')  # Obtém a senha dos dados fornecidos.

        # Verifica se o nome de usuário e a senha foram fornecidos.
        if not username or not password:
            return {"error": "Nome de usuário e senha são obrigatórios"}, 400  # Retorna erro se algum dado faltar.

        # Gera um hash para a senha.
        hashed_password = generate_password_hash(password)
        
        # Tenta criar o usuário no banco de dados. Retorna mensagem de sucesso ou erro de duplicação.
        if UserModel.create_user(username, hashed_password):
            return {"message": "Usuário registrado com sucesso"}, 201  # Retorna sucesso se o usuário for criado.
        
        return {"error": "Nome de usuário já existe"}, 400  # Retorna erro se o nome de usuário já existir.

    # Método estático para fazer o login de um usuário.
    @staticmethod
    def login_user(data):
        username = data.get('username')  # Obtém o nome de usuário dos dados fornecidos.
        password = data.get('password')  # Obtém a senha dos dados fornecidos.

        # Verifica se o nome de usuário e a senha foram fornecidos.
        if not username or not password:
            return {"error": "Nome de usuário e senha são obrigatórios"}, 400  # Retorna erro se algum dado faltar.

        # Busca o usuário no banco de dados pelo nome de usuário.
        user = UserModel.find_by_username(username)
        if user and check_password_hash(user['password'], password):  # Verifica se a senha é válida.
            access_token = create_access_token(identity=str(user['id']))  # Cria um token JWT com o ID do usuário.
            return {"access_token": access_token}, 200  # Retorna o token de acesso.

        return {"error": "Nome de usuário ou senha inválidos"}, 401  # Retorna erro se as credenciais forem inválidas.

    # Método estático para obter os dados de um usuário.
    @staticmethod
    def get_user(user_id):
        user = UserModel.find_by_id(user_id)  # Busca o usuário pelo ID.
        if user:
            return {"id": user['id'], "username": user['username']}, 200  # Retorna os dados do usuário.
        return {"error": "Usuário não encontrado"}, 404  # Retorna erro se o usuário não for encontrado.

    # Método estático para atualizar os dados de um usuário.
    @staticmethod
    def update_user(user_id, data):
        username = data.get('username')  # Obtém o nome de usuário dos dados fornecidos.
        password = data.get('password')  # Obtém a senha dos dados fornecidos.

        # Verifica se pelo menos um campo foi fornecido para atualização.
        if not username and not password:
            return {"error": "Informe ao menos um campo para atualizar"}, 400  # Retorna erro se nenhum campo for fornecido.

        # Gera um hash para a senha se a senha for fornecida.
        hashed_password = generate_password_hash(password) if password else None
        # Atualiza o usuário no banco de dados.
        UserModel.update_user(user_id, username, hashed_password)

        return {"message": "Usuário atualizado com sucesso"}, 200  # Retorna mensagem de sucesso.

    # Método estático para excluir um usuário.
    @staticmethod
    def delete_user(user_id):
        UserModel.delete_user(user_id)  # Exclui o usuário do banco de dados.
        return {"message": "Usuário deletado com sucesso"}, 200  # Retorna mensagem de sucesso.
