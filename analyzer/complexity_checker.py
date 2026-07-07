import re

def check_complexity(password):
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    complexity_score = sum([
        has_upper,
        has_lower,
        has_digit,
        has_special
    ])

    return{
        "uppercase": has_upper,
        "lowercase": has_lower,
        "digits": has_digit,
        "special": has_special,
        "score": complexity_score
    }