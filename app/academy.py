import json
import streamlit as st

from services.state_service import StateService


def show():

    st.title("🎓 Aptitude Academy")

    with open(
        "data/aptitude/academy.json",
        "r",
        encoding="utf-8"
    ) as f:

        academies = json.load(f)

    for academy in academies:

        if st.button(
            academy["name"],
            use_container_width=True
        ):

            StateService.save_academy(
                academy["folder"]
            )

            st.success(
                f"Selected {academy['name']}"
            )