import streamlit as st

from pages.academy import learning as learning_page


def show():

    st.title("📖 Learning")

    st.caption(
        "Study concepts before taking quizzes."
    )

    st.divider()

    if not st.session_state.get("selected_question_file"):

        st.info(
            "Open Academy → Select a Topic → Click Learn."
        )

        return

    learning_page.show()