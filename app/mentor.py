import streamlit as st

from services.mentor_service import MentorService


def show():

    st.title("🤖 AI Mentor")

    st.caption("Your Personal Placement Mentor")

    st.divider()

    st.subheader("📌 Daily Suggestions")

    suggestions = MentorService.get_suggestions()

    for suggestion in suggestions:

        st.success(suggestion)

    st.divider()

    question = st.text_area(
        "Ask your mentor",
        placeholder="Example: How do I improve aptitude speed?"
    )

    if st.button(
        "💬 Ask Mentor",
        use_container_width=True,
    ):

        if question.strip() == "":

            st.warning("Enter a question.")

        else:

            st.info(
                "LLM integration will be added here."
            )

    st.divider()

    st.subheader("🎯 Daily Goal")

    st.info(
        """
• Solve 20 Aptitude Questions

• Revise 2 Topics

• Attempt 1 Mock Test

• Maintain your learning streak 🔥
"""
    )