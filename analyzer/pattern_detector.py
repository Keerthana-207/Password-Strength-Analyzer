import re

COMMON_PASSWORDS = [
    "123456",
    "12345",
    "123456789"
    "password",
    "iloveyou",
    "princess",
    "1234567",
    "rockyou",
    "12345678",
    "abc123",
    "nicole",
    "daniel",
    "babygirl",
    "monkey",
    "lovely",
    "jessica",
    "654321",
    "michael",
    "ashley",
    "qwerty",
    "111111",
    "iloveu",
    "000000",
    "michelle",
    "tigger",
    "letmein",
    "admin",
    "qwerty123",
    "password123",
    "passw0rd",
    "welcome",
    "monkey",
    "donkey",
    "sunshine",
    "dragon",
    "master"
]

def detect_pattern(password):
    detected_patterns = []
    for pattern in COMMON_PASSWORDS:
        if pattern in password.lower():
            detected_patterns.append(pattern)
    if re.search(r"(.)\1{2,}",password):
        detected_patterns.append("Repeated characters")
    if re.search(r"123|234|345|456|567|678|789",password):
        detected_patterns.append("Sequential numbers")
    return {
        "has_patterns": len(detected_patterns) > 0,
        "patterns" : detected_patterns
    }
