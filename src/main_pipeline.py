from src.model.predict import predict_email
from src.explainability.shap_explainer import explain_email
from src.url_analysis.extract_url import extract_urls
from src.url_analysis.url_features import extract_url_features
from src.url_analysis.domain_info import get_domain
from src.url_analysis.url_risk_score import calculate_url_risk

from src.domain_similarity.domain_matcher import detect_typosquatting

from src.behavior_analysis.domain_age import get_domain_age
from src.behavior_analysis.behavior_risk_score import calculate_behavior_risk

from src.hybrid_analysis.hybrid_score import hybrid_analysis


def run_pipeline(email):

    # Phase 2
    bert_result = predict_email(email)
    bert_score = bert_result["score"]

    # Phase 3
    urls = extract_urls(email)

    url_score = 0
    domain_result = {"is_suspicious": False}
    behavior_score = 0

    if urls:

        url = urls[0]

        features = extract_url_features(url)

        domain = get_domain(url)

        url_score = calculate_url_risk(features, domain)

        # Phase 4
        domain_result = detect_typosquatting(domain)

        # Phase 5
        age = get_domain_age(domain)

        behavior_score = calculate_behavior_risk(age, domain)

    # Phase 6
    final_result = hybrid_analysis(
        bert_score,
        url_score,
        domain_result,
        behavior_score
    )
    if final_result["prediction"] == "PHISHING":
        shap_html = explain_email(email)
    else:
        shap_html = ""

    return {
        "bert_score": bert_score,
        "url_score": url_score,
        "domain_result": domain_result,
        "behavior_score": behavior_score,
        "final_result": final_result,
        "shap_html": shap_html
    }