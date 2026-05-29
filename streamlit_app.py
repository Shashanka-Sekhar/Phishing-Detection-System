import streamlit as st
from src.main_pipeline import run_pipeline

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="PhishBERT",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CYBERPUNK / TERMINAL THEME
# --------------------------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #050505;
    color: #00ff41;
}

/* Headers */
h1, h2, h3 {
    color: #00ff41 !important;
    font-family: 'Courier New', monospace;
}

/* Text */
p, div, span, label {
    color: #00ff41 !important;
    font-family: 'Courier New', monospace;
}

/* Text Area */
textarea {
    background-color: #000000 !important;
    color: #00ff41 !important;
    border: 1px solid #00ff41 !important;
    font-family: 'Courier New', monospace !important;
}

/* Buttons */
.stButton > button {
    background-color: #000000;
    color: #00ff41;
    border: 1px solid #00ff41;
    font-family: 'Courier New', monospace;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #00ff41;
    color: #000000;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #050505;
}

/* Code blocks */
code {
    color: #00ff41 !important;
}

/* Success box */
[data-testid="stSuccess"] {
    background-color: rgba(0,255,65,0.15);
}

/* Warning box */
[data-testid="stWarning"] {
    background-color: rgba(255,255,0,0.15);
}

/* Error box */
[data-testid="stError"] {
    background-color: rgba(255,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# ASCII BANNER
# --------------------------------------------------

st.code(r"""
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██████╗ ███████╗██████╗ ████████╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
██████╔╝███████║██║███████╗███████║██████╔╝█████╗  ██████╔╝   ██║
██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══██╗██╔══╝  ██╔══██╗   ██║
██║     ██║  ██║██║███████║██║  ██║██████╔╝███████╗██║  ██║   ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝
""")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown("""
# 🛡️ PHISHBERT TERMINAL

```bash
AI-Powered Phishing Email Detection System
Status: ONLINE
Threat Intelligence Engine: ACTIVE
```

""")

st.code("""
[ OK ] DistilBERT Model Loaded
[ OK ] URL Analysis Engine Loaded
[ OK ] Domain Similarity Detector Active
[ OK ] Behavioral Analysis Active
[ OK ] SHAP Explainability Loaded

SYSTEM STATUS: OPERATIONAL
""", language="bash")

st.markdown("""
<div style="
font-family: Courier New;
color:#00ff41;
font-size:20px;">
root@phishbert:~$ _
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# INPUT
# --------------------------------------------------

email = st.text_area(
    "Enter Email Content",
    height=250
)

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if st.button("Analyze Email"):
    if not email.strip():
        st.warning("Please enter an email.")
    else:
        with st.spinner("Analyzing Email..."):
            result = run_pipeline(email)

        prediction = result["final_result"]["prediction"]
        score = result["final_result"]["final_score"]

        st.subheader("Threat Assessment")

        if prediction == "PHISHING":
            st.error(f"🚨 THREAT LEVEL : {prediction}")
        elif prediction == "SUSPICIOUS":
            st.warning(f"⚠️ RISK LEVEL : {prediction}")
        else:
            st.success(f"✅ SYSTEM STATUS : {prediction}")

        # ------------------------------------------
        # SCORE
        # ------------------------------------------
        st.subheader("Threat Score")
        st.progress(float(score))
        st.code(
            f"Threat Probability : {score * 100:.2f}%",
            language="bash"
        )

        # ------------------------------------------
        # REASONS
        # ------------------------------------------
        st.subheader("Detection Reasons")
        reasons = result["final_result"]["reasons"]

        if reasons:
            for reason in reasons:
                st.code(f"[!] {reason}", language="bash")
        else:
            st.code("[OK] No suspicious indicators found.", language="bash")

        # ------------------------------------------
        # DOMAIN SUGGESTION
        # ------------------------------------------
        if result["domain_result"].get("show_suggestion"):
            st.subheader("Suggested Legitimate Website")
            st.info(result["domain_result"]["suggested_domain"])

        # ------------------------------------------
        # EXPLANATIONS
        # ------------------------------------------
        if prediction != "SAFE" and result["user_explanation"]:
            st.subheader("Why Was This Flagged?")
            for item in result["user_explanation"]:
                st.warning(item)

        # ------------------------------------------
        # SAFE EMAIL MESSAGE
        # ------------------------------------------
        if prediction == "SAFE":
            st.success("No significant phishing indicators were detected.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")

st.code("""
PhishBERT v1.0
Developed By:
Abhishek Ray
Shashanka Sekhar Dash
Tapan Kumar Ojha
Aurobindo Kumar Biswal

Guided By:
Dr. Rabi Prakash

ITER, Siksha 'O' Anusandhan University
""", language="bash")
