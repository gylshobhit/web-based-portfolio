import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Professional Projects")
st.markdown(
    "A summary of key projects, responsibilities, and achievements throughout my professional journey."
)

st.markdown("---")


def project_card(title, duration, client, responsibilities):
    with st.container(border=True):
        st.subheader(title)
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(f"**📅 Duration**")
            st.write(duration)

            st.markdown("**🏢 Client**")
            st.write(client)

        with col2:
            st.markdown("### Key Responsibilities & Achievements")
            for item in responsibilities:
                st.markdown(f"- {item}")

        st.markdown("")


# -------------------------------------------------------------------
# Project 1
# -------------------------------------------------------------------
project_card(
    title="Merlin Project",
    duration="Jan 2022 – Present",
    client="TELUS Communications",
    responsibilities=[
        "Enabled telecom solutions on Google Cloud Platform (GCP).",
        "Supported end-to-end cloud solution implementation and deployment.",
        "Configured Catalog and Order Management modules in the cloud environment.",
        "Migrated solutions from legacy systems to the new cloud platform.",
        "Provided cross-team knowledge transfer (KT) sessions and mentored team members.",
    ],
)

# -------------------------------------------------------------------
# Project 2
# -------------------------------------------------------------------
project_card(
    title="Singleview Upgrade Project",
    duration="Apr 2021 – Dec 2021",
    client="Inmarsat",
    responsibilities=[
        "Upgraded Singleview from version 8 to version 11.",
        "Reviewed project changes and updated configurations accordingly.",
        "Resolved defects and performed unit testing.",
        "Successfully deployed the solution to Production without issues.",
    ],
)

# -------------------------------------------------------------------
# Project 3
# -------------------------------------------------------------------
project_card(
    title="Singleview Upgrade Project",
    duration="Jul 2020 – Mar 2021",
    client="VNM Mobiles",
    responsibilities=[
        "Upgraded Singleview from version 8 to version 11.",
        "Analyzed project changes and corrected system configurations.",
        "Resolved application defects and completed unit testing.",
        "Ensured smooth implementation and successful project delivery.",
    ],
)

# -------------------------------------------------------------------
# Project 4
# -------------------------------------------------------------------
project_card(
    title="Falcon Project",
    duration="May 2016 – May 2020",
    client="TELUS Communications",
    responsibilities=[
        "Worked on the Effort & Cost Estimation tool for project development.",
        "Developed responsive web services integrating Enabler, TOCP, SFDC, and other layers.",
        "Implemented telecom product coverage validation for TELUS Canada.",
        "Developed LTE Connectivity web services for location-based validation.",
        "Successfully delivered production deployments while coordinating with onsite teams.",
    ],
)

st.markdown("---")

st.success("✔ Successfully contributed to multiple telecom transformation and cloud migration projects across TELUS, Inmarsat, and VNM Mobiles.")