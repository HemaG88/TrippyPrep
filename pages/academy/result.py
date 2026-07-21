import streamlit as st

from services.progress_service import ProgressService
from services.recent_activity_service import RecentActivityService


def show():

    result = st.session_state.get("quiz_result")

    if result is None:
        st.warning("No quiz result found.")
        return

    # ==========================================================
    # Save Progress (Only Once)
    # ==========================================================

    if not st.session_state.get("progress_saved", False):

        ProgressService.save_result(
            score=result["score"],
            total_questions=result["total"],
            accuracy=result["accuracy"],
        )

        RecentActivityService.save({

            "topic": st.session_state.selected_question_file,

            "score": result["score"],

            "total": result["total"],

            "accuracy": result["accuracy"],
        })

        st.session_state.progress_saved = True

    # ==========================================================
    # Result Screen
    # ==========================================================

    st.title("🎉 Quiz Result")

    st.success(
        f"Score : {result['score']} / {result['total']}"
    )

    st.progress(
        result["accuracy"] / 100
    )

    st.metric(
        "Accuracy",
        f"{result['accuracy']}%"
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "✅ Correct",
            result["correct"]
        )

    with c2:

        st.metric(
            "❌ Wrong",
            result["wrong"]
        )

    with c3:

        st.metric(
            "⏭ Remaining",
            result["remaining"]
        )

    st.divider()

    c1, c2 = st.columns(2)

    # ==========================================================
    # Retry Quiz
    # ==========================================================

    with c1:

        if st.button(
            "🔁 Retry Quiz",
            use_container_width=True,
        ):

            st.session_state.quiz_engine = None
            st.session_state.quiz_result = None
            st.session_state.answer_submitted = False
            st.session_state.last_answer_correct = False
            st.session_state.progress_saved = False

            st.rerun()

    # ==========================================================
    # Back To Topics
    # ==========================================================

    with c2:

        if st.button(
            "📚 Back To Topics",
            use_container_width=True,
        ):

            st.session_state.quiz_engine = None
            st.session_state.quiz_result = None
            st.session_state.selected_question_file = None
            st.session_state.learning_mode = False
            st.session_state.answer_submitted = False
            st.session_state.last_answer_correct = False
            st.session_state.progress_saved = False

            st.rerun()