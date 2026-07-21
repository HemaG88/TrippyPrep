import streamlit as st

from pages.academy import aptitude
from pages.academy import learning
from pages.academy import quiz
from pages.academy import result


def show():

    if "quiz_result" not in st.session_state:
        st.session_state.quiz_result = None

    if st.session_state.quiz_result is not None:

        result.show()
        return

    if (
        "selected_question_file" in st.session_state
        and st.session_state.selected_question_file
    ):

        if st.session_state.get(
            "learning_mode",
            False
        ):

            learning.show()

        else:

            quiz.show()

    else:

        aptitude.show()