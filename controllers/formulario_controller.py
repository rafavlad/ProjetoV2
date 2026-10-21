from models.formulario_model import FormularioModel  # Importa o modelo FormularioModel para interagir com o banco de dados.
from flask import jsonify  # Importa jsonify para criar respostas JSON.

class FormularioController:
    # Método estático para criar um novo formulário.
    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')  # Obtém o nome do formulário dos dados fornecidos.
        email = data.get('email')  # Obtém o email do formulário.
        data_nascimento = data.get('data_nascimento')  # Obtém a data de nascimento do formulário.
        cpf = data.get('cpf')  # Obtém o CPF do formulário.
        genero = data.get('genero')  # Obtém o gênero do formulário.

        # Verifica se todos os campos obrigatórios foram fornecidos.
        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400  # Retorna erro se algum campo estiver ausente.

        # Chama o método do modelo para criar o formulário no banco de dados.
        formulario = FormularioModel.create_formulario(user_id, nome, email, data_nascimento, cpf, genero)
        if formulario:
            return {"message": "Formulário criado com sucesso"}, 201  # Retorna sucesso se o formulário for criado.
        return {"error": "Erro ao criar formulário"}, 500  # Retorna erro se houver falha na criação.

    # Método estático para obter um formulário associado ao usuário.
    @staticmethod
    def get_formulario(user_id):
        # Busca o formulário no banco de dados usando o ID do usuário.
        formulario = FormularioModel.find_by_user_id(user_id)
        if formulario:
            return {"id": formulario['id'], "nome": formulario['nome'], "email": formulario['email'], 
                    "data_nascimento": formulario['data_nascimento'], "cpf": formulario['cpf'], 
                    "genero": formulario['genero']}, 200  # Retorna os dados do formulário encontrado.
        return {"error": "Formulário não encontrado"}, 404  # Retorna erro se o formulário não for encontrado.

    # Método estático para atualizar um formulário existente.
    @staticmethod
    def update_formulario(user_id, formulario_id, data):
        # Busca o formulário pelo ID fornecido.
        formulario = FormularioModel.find_by_id(formulario_id)
        
        # Verifica se o formulário existe e se pertence ao usuário.
        if not formulario or formulario['user_id'] != user_id:
            return {"error": "Formulário não encontrado ou não autorizado"}, 404  # Retorna erro se não encontrado ou não autorizado.
        
        # Obtém os novos dados do formulário ou mantém os valores antigos.
        nome = data.get('nome', formulario['nome'])
        email = data.get('email', formulario['email'])
        data_nascimento = data.get('data_nascimento', formulario['data_nascimento'])
        cpf = data.get('cpf', formulario['cpf'])
        genero = data.get('genero', formulario['genero'])

        # Chama o método do modelo para atualizar o formulário no banco de dados.
        FormularioModel.update_formulario(formulario_id, nome, email, data_nascimento, cpf, genero)
        return {"message": "Formulário atualizado com sucesso"}, 200  # Retorna sucesso após atualização.

    # Método estático para excluir um formulário existente.
    @staticmethod
    def delete_formulario(user_id, formulario_id):
        # Busca o formulário pelo ID fornecido.
        formulario = FormularioModel.find_by_id(formulario_id)
        
        # Verifica se o formulário existe e se pertence ao usuário.
        if not formulario or formulario['user_id'] != user_id:
            return {"error": "Formulário não encontrado ou não autorizado"}, 404  # Retorna erro se não encontrado ou não autorizado.
        
        # Chama o método do modelo para excluir o formulário do banco de dados.
        FormularioModel.delete_formulario(formulario_id)
        return {"message": "Formulário deletado com sucesso"}, 200  # Retorna sucesso após exclusão.
