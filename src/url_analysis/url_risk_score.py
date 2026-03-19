def calculate_url_risk(features):

    score = 0

    if features["url_length"] > 50:
        score += 0.2

    if features["num_dots"] > 3:
        score += 0.2

    if features["num_hyphens"] > 2:
        score += 0.2

    if features["has_ip"]:
        score += 0.4

    return min(score, 1)