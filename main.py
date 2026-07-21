import streamlit as st

from pages.academy import result

from app import (
    home,
    academy,
    learning,
    practice,
    interview,
    resume,
    company,
    dashboard,
    mentor,
    settings,
)

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="TrippyPrep",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# Session State
# ==========================================================

defaults = {
    "selected_question_file": None,
    "selected_topic": None,
    "selected_academy": None,
    "learning_mode": False,
    "quiz_completed": False,
    "quiz_engine": None,
    "answer_submitted": False,
    "last_answer_correct": False,
    "progress_saved": False,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("💀 TrippyPrep")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🎓 Academy",
        "📖 Learning",
        "✍ Practice",
        "🎤 Mock Interview",
        "📄 Resume Analyzer",
        "🏢 Company Preparation",
        "📊 Dashboard",
        "🤖 AI Mentor",
        "⚙ Settings",
    ],
)

# ==========================================================
# Navigation
# ==========================================================

if page == "🏠 Home":

    home.show()

elif page == "🎓 Academy":

    if st.session_state.quiz_completed:

        result.show()

    elif st.session_state.selected_question_file is not None:

        if st.session_state.learning_mode:

            learning.show()

        else:

            from pages.academy import quiz

            quiz.show()

    else:

        academy.show()

elif page == "📖 Learning":

    learning.show()

elif page == "✍ Practice":

    practice.show()

elif page == "🎤 Mock Interview":

    interview.show()

elif page == "📄 Resume Analyzer":

    resume.show()

elif page == "🏢 Company Preparation":

    company.show()

elif page == "📊 Dashboard":

    dashboard.show()

elif page == "🤖 AI Mentor":

    mentor.show()

elif page == "⚙ Settings":

    settings.show()