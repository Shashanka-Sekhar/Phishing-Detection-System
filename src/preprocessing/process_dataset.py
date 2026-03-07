import pandas as pd
from clean_text import clean_email

df = pd.read_csv("data/raw/Phishing_Email.csv")

df = df.drop(columns=["Unnamed: 0"])

df['label'] = df['Email Type'].map({
    "Safe Email": 0,
    "Phishing Email": 1
})

df = df.rename(columns={
    "Email Text": "email"
})

df = df[['email', 'label']]

df['email'] = df['email'].apply(clean_email)

df =df.dropna()

df = df[df["email"] != ""]

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("data/processed/clean_emails.csv", index=False)