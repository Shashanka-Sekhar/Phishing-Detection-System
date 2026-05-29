import re

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "suspended",
    "account",
    "password",
    "login",
    "immediately",
    "click"
]

BRANDS = [
    "paypal",
    "google",
    "amazon",
    "microsoft",
    "apple",
    "netflix",
    "bank"
]

def generate_explanation(
    email,
    bert_score,
    domain_result,
    final_result
):

    explanations = []

    # Keywords
    email_lower = email.lower()

    found_keywords = []

    for word in SUSPICIOUS_KEYWORDS:

        if word in email_lower:
            found_keywords.append(word)

    if found_keywords:

        explanations.append(
            f"Suspicious keywords detected: {', '.join(found_keywords)}"
        )

    # Brand impersonation
    for brand in BRANDS:

        if brand in email_lower:

            explanations.append(
                f"Possible brand impersonation: {brand.title()}"
            )

    # Domain similarity
    if domain_result["is_suspicious"]:

        explanations.append(
            "Domain similarity attack detected (typosquatting)"
        )

    # Confidence
    confidence = round(bert_score * 100, 2)

    explanations.append(
        f"DistilBERT phishing confidence: {confidence}%"
    )

    return explanations