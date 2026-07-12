import streamlit as st
from services.company_service import CompanyService


def show():

    st.title("🏢 Company Preparation")

    companies = CompanyService.get_companies()

    company = st.selectbox(
        "Company",
        companies
    )

    section = st.selectbox(
        "Section",
        [
            "Aptitude",
            "Technical",
            "Coding",
            "HR"
        ]
    )

    if st.button("Load Questions"):

        questions = CompanyService.load_company_questions(
            company,
            section
        )

        if not questions:

            st.warning("No questions available.")
            return

        st.success(
            f"{len(questions)} Questions Loaded"
        )

        st.markdown("---")

        for i, q in enumerate(
            questions[:5],
            start=1
        ):

            st.subheader(f"Question {i}")

            st.write(q["question"])

            if "options" in q:

                for option in q["options"]:

                    st.write(f"• {option}")

            st.markdown("---")