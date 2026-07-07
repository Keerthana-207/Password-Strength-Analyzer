def calculate_score(
        length_result,
        complexity_result,
        entropy_result,
        pattern_result,
        breach_result,
        personal_info_result
):
    score = 0
    if length_result["is_valid"]:
        score += 10
    if length_result["is_recommended"]:
        score += 10
    score += complexity_result["score"] * 5

    if entropy_result >= 75:
        score += 25
    elif entropy_result >= 50:
        score += 15
    elif entropy_result >= 28:
        score += 10

    if not pattern_result["has_patterns"]:
        score += 15

    if not breach_result["breached"]:
        score += 20

    if not personal_info_result["contains_personal_info"]:
        score += 10

    return min(score, 100)