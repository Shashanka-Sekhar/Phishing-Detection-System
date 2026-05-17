def get_domain_score(domain_result):
    """
    Convert domain similarity result into numeric score.
    
    Returns:
        1 -> suspicious / typo-squatting detected
        0 -> safe domain
    """
    return 1 if domain_result["is_suspicious"] else 0


def calculate_final_score(bert, url, domain, behavior):
    """
    Weighted hybrid phishing score calculation.

    Weights:
    BERT      = 40%
    URL       = 25%
    Domain    = 20%
    Behavior  = 15%
    """

    final_score = (
        0.4 * bert +        # Email content analysis
        0.25 * url +        # URL analysis
        0.2 * domain +      # Domain similarity / typo-squatting
        0.15 * behavior     # Sender behavior
    )

    return round(final_score, 3)


def classify_email(score):
    """
    Final classification based on hybrid score.
    
    > 0.7  -> PHISHING
    > 0.4  -> SUSPICIOUS
    <=0.4  -> SAFE
    """

    if score > 0.7:
        return "PHISHING"

    elif score > 0.4:
        return "SUSPICIOUS"

    else:
        return "SAFE"


def hybrid_analysis(bert_score, url_score, domain_result, behavior_score):
    """
    Complete hybrid phishing analysis.

    Inputs:
        bert_score      -> BERT phishing probability
        url_score       -> URL risk score
        domain_result   -> domain similarity dictionary
        behavior_score  -> sender behavior score

    Output:
        final_score
        prediction
        reasons
    """

    # Convert domain similarity to numeric score
    domain_score = get_domain_score(domain_result)

    # Final weighted score
    final_score = calculate_final_score(
        bert_score,
        url_score,
        domain_score,
        behavior_score
    )

    # Final label
    prediction = classify_email(final_score)

    reasons = []

    if prediction in ["PHISHING", "SUSPICIOUS"]:

        # Email Content
        if bert_score > 0.5:
            reasons.append(
                "Suspicious email content"
            )

        # URL
        if url_score > 0.3:
            reasons.append(
                "Suspicious URL detected"
            )

        # Domain Similarity
        if domain_score == 1:
            reasons.append(
                "Fake or similar domain detected"
            )

        # Sender Behavior
        if behavior_score > 0.3:
            reasons.append(
                "Suspicious sender behavior"
            )

        # Fallback safety
        if not reasons:
            reasons.append(
                "Potential phishing indicators detected"
            )

    else:
        # SAFE emails should NOT show phishing reasons
        reasons.append(
            "No major phishing indicators detected"
        )

    suggested_website = None

    if domain_result["is_suspicious"]:
        suggested_website = domain_result["suggested_domain"]

    # Final Output
    return {
        "final_score": final_score,
        "prediction": prediction,
        "reasons": reasons,
        "suggested_website": suggested_website
    }