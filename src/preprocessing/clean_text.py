import re
import warnings
from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning

# suppress BeautifulSoup warning
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

def clean_email(text):

    if not isinstance(text, str):
        return ""

    # remove HTML
    text = BeautifulSoup(text, "html.parser").get_text()

    # remove URLs
    text = re.sub(r'http\S+', '', text)

    # remove special characters
    text = re.sub(r'[^a-zA-Z ]', '', text)

    # lowercase
    text = text.lower()

    return text