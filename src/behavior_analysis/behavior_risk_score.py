def calculate_behavior_risk(domain_age, domain):

    from src.domain_similarity.domain_matcher import trusted_domains

    if domain in trusted_domains:
        return 0

    score = 0

    if domain_age is None:
        return 0

    if domain_age < 30:
        score += 0.5

    elif domain_age < 180:
        score += 0.3

    suspicious_words = [
        "login",
        "secure",
        "verify",
        "account",
        "update",
        "signin",
        "password"
    ]

    for word in suspicious_words:

        if word in domain.lower():

            score += 0.1

    return min(score, 1)