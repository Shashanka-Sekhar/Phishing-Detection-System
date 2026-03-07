import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

model_path = "models/phishing_email_model"

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
    prediction = torch.argmax(logits).item()

    if prediction == 1:
        return "Phishing Email"
    else:
        return "Safe Email"


email = "Your account has been suspended. Click here to verify."

result = predict_email(email)

print("Email:", email)
print("Prediction:", result)