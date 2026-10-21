import sqlite3  # Importando a biblioteca sqlite3 para interação com o banco de dados SQLite.
from database.db import get_db_connection  # Importando a função para obter uma conexão com o banco de dados.

class FormularioModel:
    # Método estático para criar um novo formulário.
    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        try:
            # Executa a inserção de um novo formulário na tabela 'formularios'.
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()  # Confirma a transação.
            return True  # Retorna True se o formulário foi criado com sucesso.
        except sqlite3.IntegrityError:
            # Caso ocorra um erro de integridade (como dados duplicados).
            return None  # Retorna None se ocorrer um erro.
        finally:
            conn.close()  # Fecha a conexão com o banco de dados.

    # Método estático para buscar um formulário pelo ID do usuário.
    @staticmethod
    def find_by_user_id(user_id):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        # Executa uma consulta SQL para buscar o formulário do usuário pelo ID.
        formulario = conn.execute('SELECT * FROM formularios WHERE user_id = ?', (user_id,)).fetchone()
        conn.close()  # Fecha a conexão com o banco de dados.
        return formulario  # Retorna o formulário encontrado (ou None, se não encontrado).

    # Método estático para buscar um formulário pelo seu ID.
    @staticmethod
    def find_by_id(formulario_id):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        # Executa uma consulta SQL para buscar o formulário pelo ID fornecido.
        formulario = conn.execute('SELECT * FROM formularios WHERE id = ?', (formulario_id,)).fetchone()
        conn.close()  # Fecha a conexão com o banco de dados.
        return formulario  # Retorna o formulário encontrado (ou None, se não encontrado).

    # Método estático para atualizar um formulário existente.
    @staticmethod
    def update_formulario(formulario_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        # Executa a atualização do formulário com os novos dados.
        conn.execute('''UPDATE formularios SET nome = ?, email = ?, data_nascimento = ?, cpf = ?, genero = ?
                         WHERE id = ?''', 
                     (nome, email, data_nascimento, cpf, genero, formulario_id))
        conn.commit()  # Confirma a transação.
        conn.close()  # Fecha a conexão com o banco de dados.

    # Método estático para excluir um formulário pelo seu ID.
    @staticmethod
    def delete_formulario(formulario_id):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        # Executa a exclusão do formulário com o ID fornecido.
        conn.execute('DELETE FROM formularios WHERE id = ?', (formulario_id,))
        conn.commit()  # Confirma a transação.
        conn.close()  # Fecha a conexão com o banco de dados.
