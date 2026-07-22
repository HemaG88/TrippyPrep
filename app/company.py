import streamlit as st

from services.company_service import CompanyService


def show():

    st.title("🏢 Company Preparation")

    st.caption("Practice company-specific preparation")

    st.divider()

    companies = CompanyService.get_companies()

    if not companies:

        st.info("No company data available.")

        return

    company = st.selectbox(

        "Select Company",

        companies,

    )

    topics = CompanyService.get_company_topics(company)

    st.divider()

    st.subheader(f"📚 {company} Roadmap")

    if not topics:

        st.warning("No topics added yet.")

    else:

        for topic in topics:

            with st.expander(topic):

                st.write(f"Practice {topic}")

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.button(

            "🚀 Start Preparation",

            use_container_width=True,

        )

    with c2:

        st.button(

            "🎯 Start Mock Interview",

            use_container_width=True,

        )