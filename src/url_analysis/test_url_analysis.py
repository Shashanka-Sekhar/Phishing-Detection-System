from extract_url import extract_urls
from url_features import extract_url_features
from domain_info import get_domain
from url_risk_score import calculate_url_risk
from domain_similarity.domain_matcher import detect_typosquatting

domain = get_domain(url)

typo_result = detect_typosquatting(domain)

email = "Click here https://paypal-login-security.ru/login"

urls = extract_urls(email)

for url in urls:
    features = extract_url_features(url)
    domain = get_domain(url)
    risk = calculate_url_risk(features, domain)

    print("URL:", url)
    print("Domain:", domain)
    print("Features:", features)
    print("Risk Score:", risk)