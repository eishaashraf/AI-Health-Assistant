import streamlit as st

st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI Health Assistant")

st.markdown("""
Welcome to the **AI Health Assistant**.

Use the navigation menu on the left to explore different health tools.

### Available Features

- 🧮 BMI Calculator
- 🤒 Symptom Checker
- 🩻 Medical Imaging
- 🥗 Healthy Lifestyle
- 🚑 First Aid Guide

---

⚠️ **Disclaimer**

This application is designed for educational purposes only.
It does not replace professional medical advice.
Always consult a qualified healthcare provider.
""")

st.sidebar.success("Select a feature from the sidebar.")