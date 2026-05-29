from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_path = "models/phishing_email_model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

print("Model loaded successfully!")