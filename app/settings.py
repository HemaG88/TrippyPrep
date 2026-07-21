import streamlit as st

from services.xp_tracker_service import XPTrackerService
from services.progress_service import ProgressService


def show():

    st.title("⚙ Settings")

    st.divider()

    st.subheader("Reset Progress")

    st.warning(
        "This will reset your quiz progress and XP."
    )

    if st.button(
        "🗑 Reset All Data",
        use_container_width=True,
    ):

        ProgressService.save_progress({

            "tests_completed": 0,

            "total_score": 0,

            "total_questions": 0,

            "best_accuracy": 0,
        })

        XPTrackerService.save({

            "xp": 0,

            "level": 1,
        })

        st.success(
            "Progress Reset Successfully."
        )

    st.divider()

    st.subheader("About")

    st.info(
        """
**TrippyPrep**

Version : 1.0

AI Placement Preparation Platform

Built with ❤️ using Python + Streamlit
"""
    )