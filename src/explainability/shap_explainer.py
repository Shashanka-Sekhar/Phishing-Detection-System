import shap

from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="models/phishing_email_model",
    tokenizer="models/phishing_email_model",
    return_all_scores=True
)

explainer = shap.Explainer(classifier)

def explain_email(text):

    shap_values = explainer([text])

    html = shap.plots.text(
        shap_values[0],
        display=False
    )

    return html