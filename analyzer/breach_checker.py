from config import Config

def load_common_passwords():
    try:
        with open(Config.COMMON_PASSWORDS_FILE, "r", encoding='utf-8') as file:
            return {line.strip().lower() for line in file.readlines()}
    except FileNotFoundError:
        return set()

COMMON_PASSWORDS = load_common_passwords()

def check_breach(password):
    is_breached = password.lower() in COMMON_PASSWORDS
    return {
        'breached': is_breached
    }