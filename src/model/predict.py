import torch
import os

from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.abspath(
    os.path.join(BASE_DIR, "../../models/phishing_email_model")
)

print("MODEL PATH:", model_path)

tokenizer = DistilBertTokenizer.from_pretrained(model_path)

model = DistilBertForSequenceClassification.from_pretrained(model_path)

model.eval()


def predict_email(email):

    inputs = tokenizer(
        email,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits

    probs = torch.nn.functional.softmax(logits, dim=1)

    phishing_score = probs[0][1].item()  # class 1 = phishing

    prediction = torch.argmax(logits).item()

    if prediction == 1:
        label = "Phishing Email"
    else:
        label = "Safe Email"

    return {
        "label": label,
        "score": phishing_score
    }


if __name__ == "__main__":
    email = "Your account has been suspended. Click here to verify."

    result = predict_email(email)

    print("Email:", email)
    print("Prediction:", result["label"])
    print("Phishing Probability:", round(result["score"], 3))