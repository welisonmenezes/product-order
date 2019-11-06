from datetime import timedelta

# Configurações de ambiente
ENV = 'development'
DEBUG = True
TEMPLATES_AUTO_RELOAD = True

# Configurações de banco de dados
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'testes'

# Configurações de segurança
SECRET_KEY = '#$#gdFDKF#993FDVKkfdkj#$$2@@@@xxdfdlafFGÇPLO^dfe__fd'
PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)
USE_PERMANENT_SESSION = True

# Configurações de upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}