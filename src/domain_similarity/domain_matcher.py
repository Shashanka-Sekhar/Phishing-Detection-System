from src.domain_similarity.levenshtein_check import get_distance
trusted_domains = {
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

def extract_main_domain(domain):

    # Remove TLD
    main_part = domain.split(".")[0].lower()

    # Split by hyphen
    first_part = main_part.split("-")[0]

    # Common phishing substitutions
    replacements = {
        "0": "o",
        "1": "l",
        "3": "e",
        "4": "a",
        "5": "s",
        "7": "t",
        "@": "a"
    }

    normalized = ""

    for char in first_part:
        normalized += replacements.get(char, char)

    return normalized


def find_closest_domain(input_domain):

    min_distance = float("inf")
    closest_domain = None

    input_name = extract_main_domain(input_domain)

    # print("Input domain:", input_domain)
    # print("Extracted input:", input_name)

    for domain in trusted_domains:

        trusted_name = extract_main_domain(domain)

        # print("Comparing with:", trusted_name)

        distance = get_distance(input_name, trusted_name)

        # print("Distance:", distance)

        if distance < min_distance:
            min_distance = distance
            closest_domain = domain

    return closest_domain, min_distance

def detect_typosquatting(input_domain):

    input_domain = input_domain.lower()

    # Exact trusted domain
    if input_domain in trusted_domains:

        return {
            "is_suspicious": False,
            "suggested_domain": None,
            "distance": 0,
            "show_suggestion": False
        }

    closest_domain, distance = find_closest_domain(input_domain)

    # Likely typo-squatting
    if distance <= 4:

        return {
            "is_suspicious": True,
            "suggested_domain": closest_domain,
            "distance": distance,
            "show_suggestion": True
        }

    # Domain is too different from any trusted domain
    return {
        "is_suspicious": False,
        "suggested_domain": None,
        "distance": distance,
        "show_suggestion": False
    }