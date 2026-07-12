import streamlit as st
import random


def show():

    st.title("🎤 Mock Interview")

    interview_type = st.selectbox(
        "Interview Type",
        [
            "HR",
            "Technical",
            "Mixed"
        ]
    )

    total_questions = st.slider(
        "Number of Questions",
        5,
        20,
        10
    )

    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False

    if "interview_current" not in st.session_state:
        st.session_state.interview_current = 0

    if "interview_answers" not in st.session_state:
        st.session_state.interview_answers = {}

    questions = [

        "Tell me about yourself.",

        "What are your strengths?",

        "What are your weaknesses?",

        "Why should we hire you?",

        "Where do you see yourself in 5 years?",

        "Explain OOP.",

        "What is Python?",

        "Difference between List and Tuple?",

        "Explain SQL JOIN.",

        "What is Machine Learning?",

        "What is DBMS?",

        "Explain Operating System."
    ]

    if st.button("Start Interview"):

        st.session_state.interview_questions = random.sample(
            questions,
            total_questions
        )

        st.session_state.interview_current = 0
        st.session_state.interview_answers = {}
        st.session_state.interview_started = True

        st.rerun()

    if st.session_state.interview_started:

        q_list = st.session_state.interview_questions

        if st.session_state.interview_current < len(q_list):

            q = q_list[
                st.session_state.interview_current
            ]

            st.progress(
                (st.session_state.interview_current + 1) /
                len(q_list)
            )

            st.subheader(
                f"Question {st.session_state.interview_current + 1}"
            )

            st.write(q)

            ans = st.text_area(
                "Your Answer",
                key=f"ans_{st.session_state.interview_current}"
            )

            if st.button("Next"):

                st.session_state.interview_answers[
                    st.session_state.interview_current
                ] = ans

                st.session_state.interview_current += 1

                st.rerun()

        else:

            st.success("🎉 Interview Completed")

            st.metric(
                "Questions Answered",
                len(st.session_state.interview_answers)
            )

            st.info(
                "AI Evaluation will be connected in the next phase."
            )

            if st.button("Start Again"):

                st.session_state.interview_started = False
                st.session_state.interview_current = 0
                st.session_state.interview_answers = {}

                st.rerun()