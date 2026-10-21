from flask import Flask  # Importando a classe Flask para criar a aplicação web.
from flask_jwt_extended import JWTManager  # Importando o JWTManager para gerenciar a autenticação JWT.
from database.db import init_db  # Importando a função para inicializar o banco de dados.
from routes.user_routes import user_bp  # Importando as rotas de usuário.
from routes.formulario_routes import formulario_bp  # Importando as rotas de formulários.

# Criando uma instância do aplicativo Flask.
app = Flask(__name__)

# Carregando a configuração do aplicativo a partir do arquivo 'config.py'.
app.config.from_pyfile('config.py')

# Inicializando o gerenciador de JWT com a instância do app Flask.
jwt = JWTManager(app)

# Inicializando o banco de dados chamando a função 'init_db'.
init_db()

# Registrando o blueprint de usuários, com o prefixo '/users' para as rotas relacionadas.
app.register_blueprint(user_bp, url_prefix='/users')

# Registrando o blueprint de formulários, com o prefixo '/formularios' para as rotas relacionadas.
app.register_blueprint(formulario_bp, url_prefix='/formularios')

# Verificando se o script está sendo executado diretamente, caso sim, inicia o servidor Flask em modo de debug.
if __name__ == '__main__':
    app.run(debug=True)
