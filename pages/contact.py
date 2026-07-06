import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Contact Us",
    page_icon="📞",
    layout="centered"
)

st.title("📞 Contact Information")
st.markdown("---")

st.subheader("Get in Touch")

st.write("**📱 Contact Number:** +91 7829682954")
st.write("**📧 Email:** gylshobhit@gmail.com")
st.write("**🏠 Address:** 19 Sahyog Nagar, Bharatpur")
st.write("**📮 PIN Code:** 321001")
st.write("**🌍 State:** Rajasthan")

st.markdown("---")

st.success("Feel free to contact us for any queries or support.")

# Optional Contact Card
with st.container():
    st.markdown(
        """
        ### 📇 Contact Card

        **Name:** Shobhit Goyal

        📞 **Phone:** +91 7829682954

        📧 **Email:** gylshobhit@gmail.com

        📍 **Address:** 19 Sahyog Nagar, Bharatpur, Rajasthan - 321001
        """
    )