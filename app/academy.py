import streamlit as st

from pages.academy import aptitude
from pages.academy import quiz
from pages.academy import learning


def show():

    st.title("🎓 Academy")

    if "selected_academy" not in st.session_state:
        st.session_state.selected_academy = None

    if "selected_question_file" not in st.session_state:
        st.session_state.selected_question_file = None

    if "learning_mode" not in st.session_state:
        st.session_state.learning_mode = False

    # ==========================================
    # Quiz / Learning Screen
    # ==========================================

    if st.session_state.selected_question_file is not None:

        if st.session_state.learning_mode:

            learning.show()

        else:

            quiz.show()

        return

    # ==========================================
    # Academy Home
    # ==========================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if st.button(
            "🧮 Aptitude",
            use_container_width=True
        ):

            st.session_state.selected_academy = "aptitude"

            st.rerun()

    with c2:

        if st.button(
            "💻 Technical",
            use_container_width=True
        ):

            st.info("Coming Soon")

    with c3:

        if st.button(
            "📝 Verbal",
            use_container_width=True
        ):

            st.info("Coming Soon")

    with c4:

        if st.button(
            "🎤 HR Interview",
            use_container_width=True
        ):

            st.info("Coming Soon")

    st.divider()

    # ==========================================
    # Aptitude Module
    # ==========================================

    if st.session_state.selected_academy == "aptitude":

        aptitude.show()