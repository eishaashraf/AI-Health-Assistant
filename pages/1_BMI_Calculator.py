import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="📏")

st.title("📏 BMI Calculator")

st.write("Calculate your Body Mass Index (BMI).")

height = st.number_input(
    "Enter your height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

weight = st.number_input(
    "Enter your weight (kg)",
    min_value=10.0,
    max_value=300.0,
    value=70.0
)

if st.button("Calculate BMI"):

    bmi = weight / ((height / 100) ** 2)

    st.subheader(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.info("Category: Underweight")
        st.write("💡 Consider a balanced diet and consult a healthcare professional if needed.")

    elif bmi < 25:
        st.success("Category: Normal Weight")
        st.write("🎉 Great! Maintain your healthy lifestyle.")

    elif bmi < 30:
        st.warning("Category: Overweight")
        st.write("🥗 Consider regular exercise and a healthier diet.")

    else:
        st.error("Category: Obesity")
        st.write("⚠️ It is recommended to consult a healthcare professional.")

st.markdown("---")
st.caption("This calculator is for educational purposes only.")