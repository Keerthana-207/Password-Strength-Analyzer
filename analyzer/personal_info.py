import re

def check_personal_info(password, name="", dob="", username="", email=""):
    password_lower = password.lower()
    matches = []
    if name:
        words = name.lower().split()

        for word in words:
            if len(word) >= 3 and word in password_lower:
                matches.append(f"Name: {word}")
    if username:
        username = username.lower()
        if len(username) >= 3 and username in password_lower:
            matches.append(f"Username: {username}")
    if email:
        local = email.split('@')[0].lower()
        if len(local) >= 3 and local in password_lower:
            matches.append(f"Email username: {local}")
    if dob:
        digits = re.sub(r"\D", "", dob)
        patterns = [
            digits,
            digits[-4:], #year
            digits[:4], #first 4 digits
            digits[:2], #date
            digits[2:4], #month
        ]
        for item in patterns:
            if item and item in password:
                matches.append(f"DOB component: {item}")
    return {
        "contains_personal_info": len(matches) > 0,
        "matches": matches
    }