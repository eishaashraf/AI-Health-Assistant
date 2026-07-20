import streamlit as st

st.set_page_config(page_title="Medical Imaging", page_icon="🩻")

st.title("🩻 Medical Imaging Explorer")

st.write("Learn about the most common medical imaging techniques used in healthcare.")

imaging = st.selectbox(
    "Select an Imaging Technique",
    [
        "MRI",
        "CT Scan",
        "PET Scan",
        "Ultrasound",
        "X-Ray"
    ]
)

if imaging == "MRI":
    st.header("🧲 MRI (Magnetic Resonance Imaging)")
    st.write("""
MRI uses strong magnetic fields and radio waves to produce detailed images of soft tissues.

### Common Uses
- Brain imaging
- Spine disorders
- Ligament injuries
- Tumor detection

### Advantages
- No ionizing radiation
- Excellent soft tissue contrast

### Limitations
- Expensive
- Longer scan time
- Not suitable for some patients with metal implants
""")

elif imaging == "CT Scan":
    st.header("🩻 CT Scan (Computed Tomography)")
    st.write("""
CT scans use X-rays to produce cross-sectional images.

### Common Uses
- Trauma
- Internal bleeding
- Lung diseases
- Cancer diagnosis

### Advantages
- Very fast
- High accuracy

### Limitations
- Uses ionizing radiation
""")

elif imaging == "PET Scan":
    st.header("☢️ PET Scan")
    st.write("""
PET scans detect metabolic activity using radioactive tracers.

### Common Uses
- Cancer staging
- Brain disorders
- Heart disease

### Advantages
- Detects disease before structural changes appear

### Limitations
- Expensive
- Limited availability
""")

elif imaging == "Ultrasound":
    st.header("🔊 Ultrasound")

    st.write("""
Ultrasound uses high-frequency sound waves.

### Common Uses
- Pregnancy
- Liver
- Kidney
- Gallbladder
- Blood flow

### Advantages
- Safe
- No radiation
- Portable

### Limitations
- Lower image quality for some organs
""")

elif imaging == "X-Ray":
    st.header("🦴 X-Ray")

    st.write("""
X-rays are the most common imaging technique.

### Common Uses
- Bone fractures
- Chest imaging
- Dental examination

### Advantages
- Fast
- Low cost

### Limitations
- Uses ionizing radiation
""")

st.markdown("---")

st.subheader("📊 Quick Comparison")

st.table({
    "Technique":["MRI","CT","PET","Ultrasound","X-Ray"],
    "Radiation":["No","Yes","Yes","No","Yes"],
    "Soft Tissue":["Excellent","Good","Good","Fair","Poor"],
    "Bone Imaging":["Good","Excellent","Poor","Poor","Excellent"]
})

st.info("Always consult a qualified healthcare professional to determine the appropriate imaging test.")