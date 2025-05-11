
import streamlit as st

st.title("ICH Risk Score Calculator for AMI-CS")

st.markdown("### Select Risk Factors")

risk_factors = {
    "VA-ECMO": 9,
    "Acute ischemic stroke": 5,
    "Thrombophilia": 2,
    "Microaxial MCS (e.g., Impella)": 2,
    "Sepsis": 2,
    "Thrombolysis": 2,
    "Acute kidney injury (AKI)": 1,
    "Age < 65 years": 1
}

selected = []
score = 0
for factor, pts in risk_factors.items():
    if st.checkbox(factor):
        selected.append(factor)
        score += pts

st.markdown("### Results")
st.write("**Total Score:**", score)

def get_risk(score):
    if score <= 5:
        return "0.52%"
    elif score <= 10:
        return "1.96%"
    elif score <= 15:
        return "7.97%"
    else:
        return "22.91%"

st.write("**Predicted ICH Risk:**", get_risk(score))
