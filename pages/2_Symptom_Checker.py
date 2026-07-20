import streamlit as st

st.set_page_config(page_title="Symptom Checker", page_icon="🩺")

st.title("🩺 Symptom Checker")

st.warning(
    "⚠️ This tool provides educational information only and does not diagnose medical conditions."
)

st.write("Select the symptoms you are experiencing:")

symptoms = st.multiselect(
    "Choose symptoms",
    [
        "Fever",
        "Cough",
        "Headache",
        "Sore Throat",
        "Fatigue",
        "Nausea",
        "Chest Pain",
        "Shortness of Breath",
        "Vomiting",
        "Diarrhea"
    ]
)

if st.button("Check Symptoms"):

    if not symptoms:
        st.warning("Please select at least one symptom.")

    else:

        st.subheader("Educational Guidance")

        if "Chest Pain" in symptoms or "Shortness of Breath" in symptoms:
            st.error("🚨 Chest pain or difficulty breathing may require immediate medical attention. Seek emergency care.")

        elif "Fever" in symptoms and "Cough" in symptoms:
            st.info("""
Possible causes may include:
- Common Cold
- Influenza (Flu)
- COVID-19
- Respiratory Infection

Consult a healthcare professional if symptoms persist.
""")

        elif "Headache" in symptoms and "Fatigue" in symptoms:
            st.info("""
Possible causes may include:
- Stress
- Dehydration
- Lack of Sleep

Drink water, rest well, and consult a healthcare professional if symptoms worsen.
""")

        elif "Nausea" in symptoms or "Vomiting" in symptoms:
            st.info("""
Possible causes may include:
- Food Poisoning
- Viral Infection
- Stomach Upset

Stay hydrated and seek medical advice if symptoms continue.
""")

        else:
            st.success("""
Your symptoms are not specific enough to provide educational guidance.

If you feel unwell, please consult a qualified healthcare professional.
""")

st.markdown("---")

st.caption("Educational use only • AI Health Assistant")