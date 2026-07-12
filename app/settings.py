import streamlit as st


def show():

    st.title("⚙️ Settings")

    st.markdown("Manage your TrippyPrep preferences.")

    st.markdown("---")

    st.subheader("Appearance")

    theme = st.selectbox(
        "Theme",
        [
            "Light",
            "Dark",
            "System Default"
        ]
    )

    st.subheader("Notifications")

    email = st.checkbox("Email Notifications")

    reminders = st.checkbox("Study Reminders")

    st.subheader("Practice")

    difficulty = st.selectbox(
        "Default Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    questions = st.slider(
        "Default Questions per Test",
        5,
        50,
        10
    )

    st.markdown("---")

    if st.button("💾 Save Settings"):

        st.success("Settings saved successfully.")

        st.write("Theme :", theme)
        st.write("Email :", email)
        st.write("Reminders :", reminders)
        st.write("Difficulty :", difficulty)
        st.write("Questions :", questions)

    st.markdown("---")

    st.info("User settings will be stored permanently in a future update.")