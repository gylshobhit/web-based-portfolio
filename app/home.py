import streamlit as st
from pathlib import Path

# ----------------------------------------
# Page Configuration
# ----------------------------------------
st.set_page_config(
    page_title="Shobhit Goyal | Java Developer",
    page_icon="💼",
    layout="wide"
)

# ----------------------------------------
# Custom CSS
# ----------------------------------------
st.markdown("""
<style>
.main{
    padding-top:2rem;
}

.big-font{
    font-size:42px;
    font-weight:700;
    color:#0E76A8;
}

.sub-font{
    font-size:22px;
    color:gray;
}

.card{
    background-color:#f8f9fa;
    padding:20px;
    border-radius:12px;
    border:1px solid #ddd;
    text-align:center;
    height:180px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:15px;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# Hero Section
# ----------------------------------------
left, right = st.columns([1, 2], gap="large")

with left:
    image_path = Path("assets/shobhit.jpeg")

    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.warning("Profile image not found.")

with right:

    st.markdown(
        '<p class="big-font">👋 Hi, I\'m Shobhit Goyal</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="sub-font">Senior Java Backend Developer | Spring Boot | Web Services</p>',
        unsafe_allow_html=True,
    )

    st.write(
        """
        I am a passionate **Java Backend Developer** with **8+ years of professional
        experience** in designing, developing, and maintaining enterprise applications.

        I specialize in developing scalable backend systems using **Java, Spring Boot,
        Hibernate, Oracle SQL, REST APIs, SOAP Web Services, and Telecom Integration**.

        I enjoy solving complex business problems and building reliable, high-performance
        applications.
        """
    )

    resume = Path("assets/resume.pdf")

    if resume.exists():
        with open(resume, "rb") as pdf:
            st.download_button(
                "📄 Download Resume",
                pdf,
                file_name="Shobhit_Goyal_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

st.divider()

# ----------------------------------------
# Professional Summary
# ----------------------------------------
st.subheader("📊 Professional Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("💼 Experience", "8+ Years")
c2.metric("🚀 Projects", "100+")
c3.metric("👨‍🏫 Mentored", "10+")
c4.metric("🏆 Client Satisfaction", "100%")

st.divider()

# ----------------------------------------
# What I Do
# ----------------------------------------
st.subheader("🚀 What I Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>☕ Java Development</h3>
    <br>
    Enterprise application development using Java,
    Spring Boot and Hibernate.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🔗 API Integration</h3>
    <br>
    REST APIs, SOAP Web Services,
    JSON, XML and System Integration.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🗄 Database Design</h3>
    <br>
    Oracle SQL, MySQL,
    PostgreSQL and Performance Tuning.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ----------------------------------------
# About Me
# ----------------------------------------
st.subheader("👨‍💻 About Me")

st.write("""
Over the last **8+ years**, I have successfully delivered enterprise-level
applications for the **Telecommunication Domain**.

My expertise includes:

- ☕ Java
- 🌱 Spring Boot
- 🔗 Hibernate
- 🗄 Oracle SQL
- 🌐 REST APIs
- 📡 SOAP Web Services
- 📄 JSON & XML
- ⚙ Maven
- 🧵 Multi-threading
- 🔄 System Integration
- 🐬 MySQL
- 🐘 PostgreSQL

I believe in writing **clean, maintainable, scalable, and production-ready code**.
""")

st.divider()

# ----------------------------------------
# Quote
# ----------------------------------------
st.info(
    "💡 *\"Code is like humor. When you have to explain it, it's bad.\"*"
)

# ----------------------------------------
# Footer
# ----------------------------------------
st.markdown(
    """
    <div class="footer">
    Made with ❤️ using Streamlit<br>
    © 2026 Shobhit Goyal
    </div>
    """,
    unsafe_allow_html=True,
)