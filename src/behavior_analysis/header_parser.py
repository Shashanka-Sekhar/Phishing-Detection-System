import re

def extract_sender(email_text):

    match = re.search(r'From:\s*([\w.-]+@[\w.-]+)', email_text)

    if match:
        return match.group(1)

    return None