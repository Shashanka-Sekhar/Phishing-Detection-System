from model.predict import predict_email

from url_analysis.extract_url import extract_urls
from url_analysis.url_features import extract_url_features
from url_analysis.domain_info import get_domain
from url_analysis.url_risk_score import calculate_url_risk

from domain_similarity.domain_matcher import detect_typosquatting

from behavior_analysis.domain_age import get_domain_age
from behavior_analysis.behavior_risk_score import calculate_behavior_risk

from hybrid_analysis.hybrid_score import hybrid_analysis

email = """
From: support@paypal-secure-login.ru

Your account has been suspended.
Click here to verify: https://g00gle-login.com
"""

bert_result = predict_email(email)
bert_score = bert_result["score"]

urls = extract_urls(email)

url_score = 0
domain_result = {"is_suspicious": False}
behavior_score = 0


if urls:

    url = urls[0]

    features = extract_url_features(url)

    domain = get_domain(url)

    url_score = calculate_url_risk(features, domain)

    domain_result = detect_typosquatting(domain)

    age = get_domain_age(domain)

    behavior_score = calculate_behavior_risk(age, domain)

final_result = hybrid_analysis(
    bert_score,
    url_score,
    domain_result,
    behavior_score
)


print("\n========== FINAL PHISHING ANALYSIS ==========")

print("BERT Score:", bert_score)

print("URL Score:", url_score)

print("Domain Result:", domain_result)

print("Behavior Score:", behavior_score)

print("\nFINAL RESULT:")
print(final_result)