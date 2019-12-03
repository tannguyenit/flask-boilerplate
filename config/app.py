import os


class App:
    DEBUG = os.getenv('DEBUG', False)

    TESTING = os.getenv('TESTING', False)

    URL = os.getenv('URL', 'http://localhost')

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')

    KEY = os.getenv('APP_KEY', 'my_key')

    ENV = os.getenv('APP_ENV', 'production')
