def generate_recommendations(
        length_result,
        complexity_result,
        pattern_result,
        breach_result,
        personal_info_result
):
    recommendations= []

    if not length_result["is_valid"]:
        recommendations.append("Increase password length to atleast 8 characters.")
    if not length_result["is_recommended"]:
        recommendations.append("Use at least 12 characters for better security.")
    if not complexity_result["uppercase"]:
        recommendations.append("Add uppercase letters.")
    if not complexity_result["lowercase"]:
        recommendations.append("Add lowercase letters.")
    if not complexity_result["digits"]:
        recommendations.append("Include numbers.")
    if not complexity_result["special"]:
        recommendations.append("Include special symbols.")
    if pattern_result["has_patterns"]:
        recommendations.append("Avoid predictable patterns like sequences or repeated characters.")
    if breach_result["breached"]:
        recommendations.append("This password appears in common leaked datasets. Avoid using it.")
    if personal_info_result["contains_personal_info"]:
        recommendations.append("Avoid using personal information such as your name, username, email, or date of birth in your password.")
    if not recommendations:
        recommendations.append("Excellent password. No major weakness detected.")
    return recommendations