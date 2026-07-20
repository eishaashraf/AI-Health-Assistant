import streamlit as st

st.set_page_config(page_title="Healthy Lifestyle", page_icon="🥗")

st.title("🥗 Healthy Lifestyle Planner")

st.write("Small healthy habits can make a big difference in your overall well-being.")

st.markdown("---")

# Water Intake Calculator
st.header("💧 Daily Water Intake Calculator")

weight = st.number_input(
    "Enter your weight (kg)",
    min_value=20,
    max_value=250,
    value=70
)

water = weight * 35

st.success(f"Recommended Daily Water Intake: **{water/1000:.1f} Liters**")

st.markdown("---")

# Exercise
st.header("🏃 Exercise Recommendations")

exercise = st.selectbox(
    "Choose your activity level",
    [
        "Beginner",
        "Moderately Active",
        "Highly Active"
    ]
)

if exercise == "Beginner":
    st.info("""
✅ Walk 30 minutes daily

✅ Stretch for 10 minutes

✅ Light yoga
""")

elif exercise == "Moderately Active":
    st.success("""
✅ 45 minutes exercise

✅ Strength training

✅ Cycling or jogging
""")

else:
    st.success("""
✅ 60–90 minutes training

✅ Cardio + Strength

✅ Proper recovery
""")

st.markdown("---")

# Sleep
st.header("😴 Sleep Recommendations")

age = st.slider("Your Age", 5, 80, 25)

if age < 18:
    st.info("Recommended Sleep: 8–10 hours")

elif age < 65:
    st.success("Recommended Sleep: 7–9 hours")

else:
    st.warning("Recommended Sleep: 7–8 hours")

st.markdown("---")

# Healthy Diet

st.header("🍎 Healthy Eating Tips")

tips = [
    "🥦 Eat more vegetables",
    "🍓 Include fruits daily",
    "🥜 Choose healthy fats",
    "🥛 Drink enough water",
    "🍟 Limit processed food",
    "🥤 Reduce sugary drinks"
]

for tip in tips:
    st.write(tip)

st.markdown("---")

st.header("✅ Daily Health Checklist")

st.checkbox("💧 Drank enough water")
st.checkbox("🥗 Ate healthy meals")
st.checkbox("🏃 Exercised today")
st.checkbox("😴 Slept 7–9 hours")
st.checkbox("🧘 Managed stress")

st.markdown("---")

st.caption("Healthy habits lead to a healthier life.")