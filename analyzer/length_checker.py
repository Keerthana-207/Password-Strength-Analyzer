from config import Config

def check_length(password):
    length = len(password)

    return{
        "length": length,
        "is_valid": length >= Config.MIN_PASSWORD_LENGTH,
        "is_recommended": length >= Config.RECOMMENDED_PASSWORD_LENGTH
    }