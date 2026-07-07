import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')

    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 5000

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    COMMON_PASSWORDS_FILE = os.path.join(
        BASE_DIR,
        'data',
        'common_passwords.txt'
    )

    MIN_PASSWORD_LENGTH = 8
    RECOMMENDED_PASSWORD_LENGTH = 12

    WEAK_ENTROPY = 28
    MODERATE_ENTROPY = 50
    STRONG_ENTROPY = 75