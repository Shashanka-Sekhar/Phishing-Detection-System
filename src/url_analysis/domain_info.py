import tldextract

def get_domain(url):

    extracted = tldextract.extract(url)

    domain = extracted.domain
    suffix = extracted.suffix

    return f"{domain}.{suffix}"