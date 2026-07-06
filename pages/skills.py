import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Technical Skills",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Technical Skills")
st.markdown("### My Technical Expertise")
st.markdown("---")

# -----------------------------
# Programming & Backend
# -----------------------------
st.subheader("☕ Programming & Backend")

col1, col2 = st.columns(2)

with col1:
    st.write("✅ Java")
    st.progress(95)

    st.write("✅ Spring Boot")
    st.progress(90)

    st.write("✅ Hibernate")
    st.progress(88)

with col2:
    st.write("✅ Multi-Threading")
    st.progress(85)

    st.write("✅ Maven")
    st.progress(90)

# -----------------------------
# Databases
# -----------------------------
st.markdown("---")
st.subheader("🗄️ Databases")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Oracle", "★★★★★")

with col2:
    st.metric("MySQL", "★★★★☆")

with col3:
    st.metric("PostgreSQL", "★★★★☆")

# -----------------------------
# APIs & Integration
# -----------------------------
st.markdown("---")
st.subheader("🔗 APIs & Integration")

skills = [
    "REST Web Services",
    "JSON",
    "XML",
    "System Integration",
    "Enterprise Integration"
]

cols = st.columns(3)

for i, skill in enumerate(skills):
    cols[i % 3].success(skill)

# -----------------------------
# Domain Knowledge
# -----------------------------
st.markdown("---")
st.subheader("📡 Domain Expertise")

st.info("""
**Telecommunication Domain**

Experience in developing and maintaining enterprise applications
for the telecom industry with exposure to system integration,
backend services, and database-driven applications.
""")

# -----------------------------
# Skill Summary
# -----------------------------
st.markdown("---")
st.subheader("📊 Skill Summary")

summary = {
    "Backend Development": "⭐⭐⭐⭐⭐",
    "Database Management": "⭐⭐⭐⭐⭐",
    "REST APIs": "⭐⭐⭐⭐☆",
    "Frameworks": "⭐⭐⭐⭐⭐",
    "Integration": "⭐⭐⭐⭐☆",
    "Problem Solving": "⭐⭐⭐⭐⭐"
}

for key, value in summary.items():
    st.write(f"**{key}**")
    st.write(value)

st.markdown("---")

st.success(
    "Experienced in building enterprise Java applications using Spring Boot, "
    "Hibernate, relational databases, RESTful Web Services, and integration technologies."
)