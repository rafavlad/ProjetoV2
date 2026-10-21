import os

SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
JWT_SECRET_KEY = SECRET_KEY
DATABASE = 'database.db'