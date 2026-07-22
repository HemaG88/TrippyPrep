import streamlit as st

from services.report_service import ReportService


def show():

    st.title("🚩 Reported Questions")

    reports = ReportService.load()

    if not reports:

        st.info("No reported questions.")

        return

    st.metric(
        "Total Reports",
        len(reports)
    )

    st.divider()

    for i, question in enumerate(reports, start=1):

        with st.expander(
            f"Question {i}"
        ):

            st.write(question["question"])

            st.write("### Options")

            for option in question["options"]:

                st.write(f"• {option}")

            st.divider()

            st.success(
                f"Correct Answer: Option {question['correct_option']}"
            )

            st.write(
                question.get(
                    "explanation",
                    "No explanation available."
                )
            )