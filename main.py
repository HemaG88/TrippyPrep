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

st.set_page_config(
    page_title="TrippyPrep",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded",
)

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

if page == "🏠 Home":
    home.show()

elif page == "🎓 Academy":

    if st.session_state.get("quiz_completed", False):

        result.show()

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