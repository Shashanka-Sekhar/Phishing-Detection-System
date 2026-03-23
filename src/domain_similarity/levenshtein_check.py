import Levenshtein

def get_distance(domain1, domain2):
    return Levenshtein.distance(domain1, domain2)