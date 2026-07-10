import streamlit as st


def show():

    st.title("💀 TrippyPrep")

    st.subheader("Your Personal Placement Preparation Companion")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.info("📚 Learn")

        st.info("✍ Practice")

        st.info("📝 Test")

    with col2:

        st.info("📊 Progress")

        st.info("🏆 Badges")

        st.info("🤖 AI Mentor")

    st.divider()

    st.success("Select an option from the left sidebar to begin.")