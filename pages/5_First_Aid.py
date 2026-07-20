import streamlit as st

st.set_page_config(page_title="First Aid Guide", page_icon="🚑")

st.title("🚑 First Aid Guide")

st.warning("⚠️ This information is for educational purposes only. In a medical emergency, contact your local emergency services immediately.")

st.markdown("---")

topic = st.selectbox(
    "Choose an emergency",
    [
        "Heart Attack",
        "Burns",
        "Bleeding",
        "Choking",
        "Snake Bite",
        "Electric Shock"
    ]
)

if topic == "Heart Attack":
    st.header("❤️ Heart Attack")
    st.write("""
- Call emergency services immediately.
- Help the person sit comfortably.
- Loosen tight clothing.
- If prescribed, assist with their medication.
- Begin CPR only if trained and the person becomes unresponsive.
""")

elif topic == "Burns":
    st.header("🔥 Burns")
    st.write("""
- Cool the burn with cool running water for about 20 minutes.
- Remove tight items if possible.
- Cover with a clean, non-stick dressing.
- Do not apply ice or butter.
- Seek medical care for severe burns.
""")

elif topic == "Bleeding":
    st.header("🩸 Bleeding")
    st.write("""
- Apply firm pressure using a clean cloth or bandage.
- Keep pressure on the wound.
- Raise the injured area if appropriate.
- Seek emergency help if bleeding is severe or won't stop.
""")

elif topic == "Choking":
    st.header("🤧 Choking")
    st.write("""
- Encourage coughing if the person can cough.
- If they cannot breathe or speak, seek emergency help immediately.
- Trained rescuers may perform appropriate first-aid maneuvers.
""")

elif topic == "Snake Bite":
    st.header("🐍 Snake Bite")
    st.write("""
- Keep the person calm.
- Keep the bitten limb still and below heart level if possible.
- Remove rings or tight clothing.
- Do not cut the wound or try to suck out venom.
- Get emergency medical help immediately.
""")

elif topic == "Electric Shock":
    st.header("⚡ Electric Shock")
    st.write("""
- Turn off the power source if it is safe to do so.
- Do not touch the person until the electrical source is disconnected.
- Call emergency services.
- Check breathing and responsiveness.
- Begin CPR only if trained and necessary.
""")

st.markdown("---")
st.success("Learning basic first aid can help you respond more effectively in emergencies.")