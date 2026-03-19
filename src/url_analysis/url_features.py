import re

def extract_url_features(url):

    features = {}

    features["url_length"] = len(url)

    features["num_dots"] = url.count(".")

    features["num_hyphens"] = url.count("-")

    features["has_ip"] = bool(re.search(r'\d+.\d+.\d+.\d+', url))

    return features