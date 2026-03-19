import whois
import requests

def check_phishtank(url):

    response = requests.post(
        "http://checkurl.phishtank.com/checkurl/",
        data={"url": url}
    )

    return response.text
def get_domain_age(domain):

    try:

        w = whois.whois(domain)

        return w.creation_date

    except:
        return None