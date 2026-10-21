import sqlite3  # Importando a biblioteca sqlite3 para interação com o banco de dados SQLite.
from database.db import get_db_connection  # Importando a função para obter uma conexão com o banco de dados.

class UserModel:
    # Método estático para buscar um usuário pelo nome de usuário.
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        # Executa uma consulta SQL para buscar o usuário com o nome de usuário fornecido.
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()  # Fecha a conexão com o banco de dados.
        return user  # Retorna o usuário encontrado (ou None, se não encontrado).

    # Método estático para buscar um usuário pelo ID.
    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        # Executa uma consulta SQL para buscar o usuário com o ID fornecido.
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()  # Fecha a conexão com o banco de dados.
        return user  # Retorna o usuário encontrado (ou None, se não encontrado).

    # Método estático para criar um novo usuário.
    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        try:
            # Executa a inserção do novo usuário na tabela 'users'.
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()  # Confirma a transação.
            return True  # Retorna True se o usuário foi criado com sucesso.
        except sqlite3.IntegrityError:
            # Caso ocorra um erro de integridade (como tentativa de criar um usuário com nome duplicado).
            return None  # Retorna None se ocorrer um erro.
        finally:
            conn.close()  # Fecha a conexão com o banco de dados.

    # Método estático para atualizar os dados de um usuário (nome de usuário ou senha).
    @staticmethod
    def update_user(user_id, username=None, password=None):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.

        # Se o nome de usuário foi fornecido, atualiza o nome de usuário.
        if username:
            conn.execute('UPDATE users SET username = ? WHERE id = ?', (username, user_id))
        # Se a senha foi fornecida, atualiza a senha.
        if password:
            conn.execute('UPDATE users SET password = ? WHERE id = ?', (password, user_id))

        conn.commit()  # Confirma a transação.
        conn.close()  # Fecha a conexão com o banco de dados.

    # Método estático para excluir um usuário.
    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()  # Obtém uma conexão com o banco de dados.
        # Executa a exclusão do usuário com o ID fornecido.
        conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()  # Confirma a transação.
        conn.close()  # Fecha a conexão com o banco de dados.
