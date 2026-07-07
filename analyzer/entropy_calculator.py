import math
import re

def calculate_entropy(password):
    charset_size = 0

    if re.search(r"[A-Z]",password):
        charset_size += 26
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"\d",password):
        charset_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]",password):
        charset_size += 32
    if charset_size == 0:
        return 0
    entropy = len(password) * math.log2(charset_size)
    return round(entropy,2)
