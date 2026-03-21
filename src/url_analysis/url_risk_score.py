def calculate_url_risk(features, domain):

    score = 0

    if features["url_length"] > 30:
        score += 0.2

    if features["num_dots"] >= 2:
        score += 0.2

    if features["num_hyphens"] >= 1:
        score += 0.2

    if features["has_ip"]:
        score += 0.3

    suspicious_words = ["login", "verify", "secure", "account", "update"]

    for word in suspicious_words:
        if word in domain:
            score += 0.1

    return min(score, 1)