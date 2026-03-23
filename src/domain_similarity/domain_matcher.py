trusted_domains = [
"google.com", "amazon.com", "facebook.com", "apple.com", "microsoft.com", "paypal.com", "netflix.com", "yahoo.com", "youtube.com", "linkedin.com", "instagram.com", "twitter.com", "chase.com", "wellsfargo.com", "bankofamerica.com", "ebay.com", "walmart.com", "whatsapp.com", "wikipedia.org", "reddit.com", "adobe.com", "dropbox.com", "github.com", "roblox.com", "twitch.tv", "steamcommunity.com", "coinbase.com", "binance.com", "dhl.com", "fedex.com", "usps.com", "ups.com", "instagram.com", "tiktok.com", "pinterest.com", "spotify.com", "wordpress.com", "tumblr.com", "bbc.co.uk", "cnn.com", "nytimes.com", "zillow.com", "booking.com", "airbnb.com", "expedia.com", "uber.com", "lyft.com", "alibaba.com", "aliexpress.com", "etsy.com"
]
from levenshtein_check import get_distance

def extract_main_domain(domain):
    return domain.split(".")[0]


def find_closest_domain(input_domain):

    min_distance = float("inf")
    closest_domain = None

    input_name = extract_main_domain(input_domain)

    print("Input domain:", input_domain)
    print("Extracted input:", input_name)

    for domain in trusted_domains:

        trusted_name = extract_main_domain(domain)

        print("Comparing with:", trusted_name)

        distance = get_distance(input_name, trusted_name)

        print("Distance:", distance)

        if distance < min_distance:
            min_distance = distance
            closest_domain = domain

    return closest_domain, min_distance

def detect_typosquatting(input_domain):

    closest_domain, distance = find_closest_domain(input_domain)

    if distance <= 2:
        return {
            "is_suspicious": True,
            "suggested_domain": closest_domain,
            "distance": distance
        }

    return {
        "is_suspicious": False,
        "suggested_domain": None,
        "distance": distance
    }
