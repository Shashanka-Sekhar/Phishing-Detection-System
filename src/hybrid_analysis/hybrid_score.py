def get_domain_score(domain_result):
    return 1 if domain_result["is_suspicious"] else 0

def calculate_final_score(bert, url, domain, behavior):

    final_score = (
        0.4 * bert +       # BERT (most important)
        0.25 * url +       # URL analysis
        0.2 * domain +     # domain similarity
        0.15 * behavior    # sender behavior
    )

    return round(final_score, 3)

def classify_email(score):

    if score > 0.7:
        return "PHISHING"
    elif score > 0.4:
        return "SUSPICIOUS"
    else:
        return "SAFE"
    
def hybrid_analysis(bert_score, url_score, domain_result, behavior_score):

    domain_score = get_domain_score(domain_result)

    final_score = calculate_final_score(
        bert_score,
        url_score,
        domain_score,
        behavior_score
    )

    prediction = classify_email(final_score)

    reasons = []

    if bert_score > 0.7:
        reasons.append("Suspicious email content")

    if url_score > 0.5:
        reasons.append("Suspicious URL detected")

    if domain_score == 1:
        reasons.append("Fake or similar domain detected")

    if behavior_score > 0.4:
        reasons.append("Suspicious sender behavior")

    return {
        "final_score": final_score,
        "prediction": prediction,
        "reasons": reasons
    }