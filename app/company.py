import streamlit as st

from services.company_service import CompanyService
from services.company_stats_service import CompanyStatsService


def show():

    st.title("🏢 Company Preparation")

    stats = CompanyStatsService.get_stats()

    st.subheader("Company Question Bank")

    cols = st.columns(3)

    for i, (company, total) in enumerate(stats.items()):

        cols[i % 3].metric(
            company,
            f"{total} Questions"
        )

    st.markdown("---")

    companies = CompanyService.get_companies()

    company = st.selectbox(
        "Select Company",
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

        if len(questions) == 0:

            st.warning("No questions found.")

            return

        st.success(
            f"{len(questions)} Questions Loaded"
        )

        st.markdown("---")

        for i, q in enumerate(questions[:5], start=1):

            with st.expander(f"Question {i}"):

                st.write(q["question"])

                if "options" in q:

                    for option in q["options"]:

                        st.write(f"• {option}")

                if "correct_option" in q:

                    st.success(q["correct_option"])

                if "explanation" in q:

                    st.info(q["explanation"])