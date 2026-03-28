from header_parser import extract_sender
from sender_check import get_sender_domain
from domain_age import get_domain_age
from behavior_risk_score import calculate_behavior_risk

email = """
From: support@paypal-secure-login.ru
Subject: Verify your account
"""

sender = extract_sender(email)

domain = get_sender_domain(sender)

age = get_domain_age(domain)

risk = calculate_behavior_risk(age, domain)

print("Sender:", sender)
print("Domain:", domain)
print("Domain Age (days):", age)
print("Behavior Risk Score:", risk)