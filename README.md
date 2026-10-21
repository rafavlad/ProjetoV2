# API de Cadastro, Login e Formulário (Flask + JWT)

API REST em Python/Flask com cadastro e login de usuários, autenticação por token JWT, senhas criptografadas (hash) e um formulário de dados pessoais vinculado a cada usuário. O banco de dados é SQLite.

## Tecnologias

- Python 3
- Flask
- Flask-JWT-Extended (autenticação por token JWT)
- SQLite (módulo `sqlite3`)
- Werkzeug (hash de senhas)
- Gunicorn (para execução em produção)

## Estrutura do projeto

```
Teste_corrigido/
├── app.py                  # Cria o app, registra os blueprints e inicia o servidor
├── config.py               # Configurações (chave JWT e nome do banco)
├── requirements.txt        # Dependências
├── database.db             # Banco SQLite
├── database/
│   └── db.py               # Conexão e criação das tabelas
├── models/                 # Acesso ao banco (consultas SQL)
│   ├── user_model.py
│   └── formulario_model.py
├── controllers/            # Regras de negócio e validações
│   ├── user_controller.py
│   └── formulario_controller.py
└── routes/                 # Rotas da API (blueprints)
    ├── user_routes.py
    └── formulario_routes.py
```

O projeto segue uma divisão em camadas: **routes → controllers → models → database**.

## Como executar

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. (Opcional) Defina a chave secreta do JWT:

   ```bash
   export JWT_SECRET_KEY="uma-chave-bem-secreta"      # Linux/macOS
   set JWT_SECRET_KEY=uma-chave-bem-secreta           # Windows (cmd)
   ```

   Se não for definida, é usada uma chave padrão, indicada apenas para testes.

4. Inicie a aplicação:

   ```bash
   python app.py
   ```

   A API ficará disponível em `http://127.0.0.1:5000`. As tabelas são criadas automaticamente na primeira execução.

## Autenticação

1. Cadastre-se em `POST /users/register`.
2. Faça login em `POST /users/login` e copie o `access_token` retornado.
3. Nas rotas protegidas, envie o token no cabeçalho:

   ```
   Authorization: Bearer <access_token>
   ```

## Endpoints

### Usuários (`/users`)

| Método | Rota              | Protegida | Descrição                          |
|--------|-------------------|-----------|------------------------------------|
| POST   | `/users/register` | Não       | Cadastra um novo usuário           |
| POST   | `/users/login`    | Não       | Autentica e retorna o token JWT    |
| GET    | `/users/me`       | Sim       | Retorna os dados do usuário logado |
| PUT    | `/users/me`       | Sim       | Atualiza usuário e/ou senha        |
| DELETE | `/users/me`       | Sim       | Exclui o usuário logado            |

### Formulários (`/formularios`)

| Método | Rota                | Protegida | Descrição                              |
|--------|---------------------|-----------|----------------------------------------|
| POST   | `/formularios/`     | Sim       | Cria um formulário para o usuário      |
| GET    | `/formularios/`     | Sim       | Retorna o formulário do usuário logado |
| PUT    | `/formularios/<id>` | Sim       | Atualiza um formulário seu             |
| DELETE | `/formularios/<id>` | Sim       | Exclui um formulário seu               |

## Exemplos de uso

**Cadastro**

```bash
curl -X POST http://127.0.0.1:5000/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "maria", "password": "123456"}'
```

Resposta (201): `{"message": "Usuário registrado com sucesso"}`

**Login**

```bash
curl -X POST http://127.0.0.1:5000/users/login \
  -H "Content-Type: application/json" \
  -d '{"username": "maria", "password": "123456"}'
```

Resposta (200): `{"access_token": "<token>"}`

**Criar formulário**

```bash
curl -X POST http://127.0.0.1:5000/formularios/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
        "nome": "Maria Souza",
        "email": "maria@example.com",
        "data_nascimento": "1995-04-20",
        "cpf": "12345678900",
        "genero": "Feminino"
      }'
```

Resposta (201): `{"message": "Formulário criado com sucesso"}`

**Atualizar formulário** (apenas os campos enviados são alterados)

```bash
curl -X PUT http://127.0.0.1:5000/formularios/1 \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"email": "novo@example.com"}'
```

## Códigos de resposta

| Código | Significado                                              |
|--------|----------------------------------------------------------|
| 200    | Operação realizada com sucesso                           |
| 201    | Recurso criado                                           |
| 400    | Dados obrigatórios ausentes ou usuário já existente      |
| 401    | Usuário ou senha inválidos / token ausente ou inválido   |
| 404    | Recurso não encontrado ou sem permissão de acesso        |

## Banco de dados

**users**: `id`, `username` (único), `password` (hash)

**formularios**: `id`, `user_id` (chave estrangeira para `users`), `nome`, `email`, `data_nascimento`, `cpf`, `genero`

## Segurança

- As senhas são armazenadas com hash (`generate_password_hash`), nunca em texto puro.
- As consultas SQL usam parâmetros (`?`), o que evita SQL injection.
- As rotas protegidas exigem um token JWT válido.
- Cada usuário só consegue alterar ou excluir os próprios formulários.
- Em produção, defina a variável `JWT_SECRET_KEY` e desative o `debug=True` do `app.py`.
