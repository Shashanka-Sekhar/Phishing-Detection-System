import streamlit as st
from src.main_pipeline import run_pipeline

st.set_page_config(
    page_title="PhishBERT",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI based Phishing Email Detection System with Behavioral Analysis and Explainable Intelligence")

st.write(
    "Detect phishing emails using DistilBERT, URL Analysis, "
    "Domain Similarity Detection, and SHAP Explainability."
)

email = st.text_area(
    "Enter Email Content",
    height=250
)

if st.button("Analyze Email"):

    if not email.strip():

        st.warning("Please enter an email.")

    else:

        with st.spinner("Analyzing Email..."):

            result = run_pipeline(email)

        prediction = result["final_result"]["prediction"]
        score = result["final_result"]["final_score"]

        st.subheader("Prediction")

        if prediction == "PHISHING":
            st.error(prediction)

        elif prediction == "SUSPICIOUS":
            st.warning(prediction)

        else:
            st.success(prediction)

        st.write(f"Final Score: {score}")

        st.subheader("Reasons")

        reasons = result["final_result"]["reasons"]

        if reasons:
            for reason in reasons:
                st.write(f"• {reason}")
        else:
            st.write("No suspicious indicators found.")

        # Show suggested website only when a meaningful match exists
        if result["domain_result"].get("show_suggestion"):

            st.subheader("Suggested Legitimate Website")

            st.info(
                result["domain_result"]["suggested_domain"]
            )

        # Show detailed explanation only for suspicious emails
        if prediction != "SAFE" and result["user_explanation"]:

            st.subheader("Why was this flagged?")

            for item in result["user_explanation"]:

                st.warning(item)

        # Optional message for SAFE emails
        if prediction == "SAFE":

            st.success(
                "No significant phishing indicators were detected."
            )