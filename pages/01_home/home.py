import streamlit as st

st.set_page_config(
    page_title="TrippyPrep",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 TrippyPrep")
st.subheader("AI-Powered Placement Preparation Platform")

st.markdown("---")

st.write("""
Welcome to **TrippyPrep**.

Your all-in-one platform for placement preparation.

Use the navigation menu to access:

- 📚 Placement Academy
- 📝 Practice Questions
- 🎯 Mock Interviews
- 📄 Resume Analyzer
- 🏢 Company-wise Preparation
- 🤖 AI Mentor
- 📊 Progress Dashboard
- ⚙️ Settings
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Questions", "2500+")

with col2:
    st.metric("Companies", "12+")

with col3:
    st.metric("Mock Tests", "100+")

st.markdown("---")

st.info("💡 Select a module from the sidebar to start your preparation.")