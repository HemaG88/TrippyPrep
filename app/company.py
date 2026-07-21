import streamlit as st

from services.company_service import CompanyService


def show():

    st.title("🏢 Company Preparation")

    st.caption(
        "Practice company-specific questions."
    )

    st.divider()

    companies = CompanyService.get_companies()

    if not companies:

        st.info(
            "No company data available."
        )

        return

    company = st.selectbox(
        "Select Company",
        companies,
    )

    st.success(
        f"Selected : {company}"
    )

    st.divider()

    st.subheader("Features")

    st.checkbox(
        "Aptitude Questions",
        value=True,
        disabled=True,
    )

    st.checkbox(
        "Technical Questions",
        value=True,
        disabled=True,
    )

    st.checkbox(
        "HR Questions",
        value=True,
        disabled=True,
    )

    st.checkbox(
        "Coding Questions",
        value=True,
        disabled=True,
    )

    st.checkbox(
        "Interview Experience",
        value=False,
        disabled=True,
    )

    st.checkbox(
        "Mock Interview",
        value=False,
        disabled=True,
    )

    st.divider()

    st.button(
        "🚀 Start Preparation",
        use_container_width=True,
    )