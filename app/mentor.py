import streamlit as st


def show():

    st.title("🤖 AI Mentor")

    st.write("Your personal AI Placement Mentor.")

    st.markdown("---")

    goal = st.selectbox(
        "Current Goal",
        [
            "Internship",
            "Placement",
            "Product Company",
            "Service Company",
            "Higher Studies"
        ]
    )

    hours = st.slider(
        "Study Hours / Day",
        1,
        12,
        4
    )

    level = st.selectbox(
        "Current Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("Generate Plan"):

        st.success("Personal Study Plan")

        st.markdown("---")

        st.write(f"🎯 Goal : {goal}")
        st.write(f"📚 Study Hours : {hours}")
        st.write(f"⭐ Level : {level}")

        st.markdown("---")

        st.subheader("Today's Tasks")

        st.checkbox("Aptitude Practice")
        st.checkbox("Technical Questions")
        st.checkbox("Company Preparation")
        st.checkbox("Mock Interview")
        st.checkbox("Resume Improvement")

        st.markdown("---")

        st.info("AI-generated personalized roadmap will be integrated soon.")

    st.markdown("---")

    st.subheader("Daily Motivation")

    st.success(
        "Small progress every day leads to big success."
    )