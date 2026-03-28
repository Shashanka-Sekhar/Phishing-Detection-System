def calculate_behavior_risk(domain_age, domain):

    score = 0

    if domain_age is None:
        score += 0.4
    elif domain_age < 30:
        score += 0.5
    elif domain_age < 180:
        score += 0.3

    suspicious_words = ["login", "secure", "verify", "account"]

    for word in suspicious_words:
        if word in domain:
            score += 0.1

    return min(score, 1)