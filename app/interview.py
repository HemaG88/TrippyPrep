import streamlit as st


def show():

    st.title("🎤 Mock Interview")

    st.caption(
        "Practice Company Interviews"
    )

    st.divider()

    interview_type = st.selectbox(

        "Interview Type",

        [

            "HR Interview",

            "Technical Interview",

            "Aptitude Interview",

            "Mixed Interview",

        ],

    )

    questions = st.slider(

        "Number of Questions",

        5,

        20,

        10,

    )

    difficulty = st.selectbox(

        "Difficulty",

        [

            "Easy",

            "Medium",

            "Hard",

        ],

    )

    st.divider()

    st.checkbox(

        "🎙 Voice Interview",

        value=False,

        disabled=True,

    )

    st.checkbox(

        "📹 Camera Analysis",

        value=False,

        disabled=True,

    )

    st.checkbox(

        "🤖 AI Feedback",

        value=True,

        disabled=True,

    )

    st.divider()

    st.success(f"Interview : {interview_type}")

    st.write(f"Questions : {questions}")

    st.write(f"Difficulty : {difficulty}")

    st.divider()

    st.button(

        "🚀 Start Interview",

        use_container_width=True,

    )