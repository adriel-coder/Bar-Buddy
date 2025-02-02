class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Password123@localhost/bar_buddy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'

class TestConfig(Config):
    """Configuração para testes"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Usa SQLite em memória
    TESTING = True
    WTF_CSRF_ENABLED = False  # Se usar Flask-WTF, desativa CSRF nos testes
