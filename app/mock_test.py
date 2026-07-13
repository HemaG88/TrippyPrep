import streamlit as st

from services.test_service import TestService


def show():

    st.title("📝 Mock Test")

    topics = [

        "aptitude/01_foundation/percentage.json",

        "aptitude/01_foundation/profit_loss.json",

        "aptitude/01_foundation/average.json",

        "aptitude/02_arithmetic/ages.json",

        "aptitude/02_arithmetic/time_and_work.json",

    ]

    if st.button("Generate Mock Test"):

        questions = TestService.generate_mock_test(
            topics,
            2
        )

        st.success(
            f"{len(questions)} Questions Generated"
        )

        st.markdown("---")

        for i, q in enumerate(
            questions,
            start=1
        ):

            st.write(f"### Q{i}")

            st.write(q["question"])

            for option in q["options"]:

                st.write(f"• {option}")

            st.markdown("---")