def calculate_behavior_risk(domain_age):

    score = 0

    # Newly created domain → suspicious
    if domain_age is not None:

        if domain_age < 30:
            score += 0.5

        elif domain_age < 180:
            score += 0.3

    else:
        score += 0.4  # unknown domain

    return min(score, 1)