from extract_urls import extract_urls

email = """
Your account has been suspended.
Click here: https://paypal-login-security.ru/login
"""

urls = extract_urls(email)

print(urls)