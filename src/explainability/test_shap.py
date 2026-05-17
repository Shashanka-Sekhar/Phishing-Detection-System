from src.explainability.shap_explainer import explain_email

text = """
Your account has been suspended.
Verify immediately.
"""

result = explain_email(text)

print(result)