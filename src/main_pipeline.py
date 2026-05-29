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
from src.explainability.explanation_generator import generate_explanation


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
        trusted_domain_list = {
                "google.com", "amazon.com", "facebook.com", "apple.com", "microsoft.com", "paypal.com", "netflix.com", "yahoo.com", "youtube.com", "linkedin.com", "instagram.com", "twitter.com", "chase.com", "wellsfargo.com", "bankofamerica.com", "ebay.com", "walmart.com", "whatsapp.com", "wikipedia.org", "reddit.com", "adobe.com", "dropbox.com", "github.com", "roblox.com", "twitch.tv", "steamcommunity.com", "coinbase.com", "binance.com", "dhl.com", "fedex.com", "usps.com", "ups.com", "instagram.com", "tiktok.com", "pinterest.com", "spotify.com", "wordpress.com", "tumblr.com", "bbc.co.uk", "cnn.com", "nytimes.com", "zillow.com", "booking.com", "airbnb.com", "expedia.com", "uber.com", "lyft.com", "alibaba.com", "aliexpress.com", "etsy.com", "hdfcbank.com",
                "icicibank.com",
                "sbi.co.in",
                "axisbank.com",
                "kotak.com",
                "indusind.com",
                "yesbank.in",
                "idbibank.in",
                "bankofbaroda.in",
                "pnbindia.in",
                "unionbankofindia.co.in",
                "canarabank.com",
                "centralbankofindia.co.in",
                "indianbank.in",
                "iob.in",
                "ucobank.com",
                "bankofindia.co.in",
                "federalbank.co.in",
                "southindianbank.com",
                "bandhanbank.com",
                "rblbank.com",
                "idfcfirstbank.com",
                "ausmallfinancebank.com",
                "equitasbank.com",
                "ujjivan.com",
                "kvb.co.in",
                "paytm.com",
                "phonepe.com",
                "bharatpe.com",
                "mobikwik.com",
                "freecharge.in",
                "cred.club",
                "rbi.org.in",
                "npci.org.in",
                "india.gov.in",
                "incometax.gov.in",
                "uidai.gov.in",
                "epfindia.gov.in",
                "parivahan.gov.in",
                "passportindia.gov.in",
                "gst.gov.in",
                "digilocker.gov.in",
                "flipkart.com",
                "myntra.com",
                "ajio.com",
                "tatacliq.com",
                "jiomart.com",
                "snapdeal.com",
                "nykaa.com",
                "firstcry.com",
                "bigbasket.com",
                "lenskart.com",
                "jio.com",
                "airtel.in",
                "vi.in",
                "bsnl.co.in",
                "tcs.com",
                "infosys.com",
                "wipro.com",
                "hcltech.com",
                "techmahindra.com",
                "ltimindtree.com",
                "persistent.com",
                "mphasis.com",
                "zoho.com",
                "irctc.co.in",
                "makemytrip.com",
                "goibibo.com",
                "yatra.com",
                "cleartrip.com",
                "redbus.in",
                "ixigo.com"
                }
        
        if domain in trusted_domain_list:

            # reduce BERT influence for known legitimate domains
            bert_score *= 0.5

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

    user_explanation = generate_explanation(
        email,
        bert_score,
        domain_result,
        final_result
    )

    return {
    "bert_score": bert_score,
    "url_score": url_score,
    "domain_result": domain_result,
    "behavior_score": behavior_score,
    "final_result": final_result,
    "shap_html": shap_html,
    "user_explanation": user_explanation
}