import sqlite3  # Importa a biblioteca sqlite3 para trabalhar com o banco de dados SQLite.
from config import DATABASE  # Importa o nome do banco de dados a partir do arquivo de configuração.

# Função para obter a conexão com o banco de dados.
def get_db_connection():
    conn = sqlite3.connect(DATABASE)  # Estabelece a conexão com o banco de dados especificado em DATABASE.
    conn.row_factory = sqlite3.Row  # Configura o factory para retornar resultados como dicionários (linhas como dicionários).
    return conn  # Retorna a conexão estabelecida.

def init_db():
    conn = get_db_connection()
    
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS formularios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        cpf TEXT NOT NULL,
        genero TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')

    conn.commit()
    conn.close()
