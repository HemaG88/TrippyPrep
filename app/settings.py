import streamlit as st

from services.settings_service import SettingsService
from services.export_service import ExportService


def show():

    st.title("⚙ Settings")

    settings = SettingsService.load()

    st.divider()

    settings["dark_mode"] = st.toggle(
        "🌙 Dark Mode",
        value=settings["dark_mode"]
    )

    settings["sound"] = st.toggle(
        "🔊 Sound",
        value=settings["sound"]
    )

    settings["notifications"] = st.toggle(
        "🔔 Notifications",
        value=settings["notifications"]
    )

    settings["daily_goal"] = st.slider(
        "🎯 Daily Goal",
        min_value=5,
        max_value=100,
        value=settings["daily_goal"],
        step=5
    )

    st.divider()

    if st.button(
        "💾 Save Settings",
        use_container_width=True
    ):

        SettingsService.save(settings)

        st.success(
            "Settings saved successfully."
        )
    st.divider()

if st.button(
    "📥 Export My Progress",
    use_container_width=True
):

    file = ExportService.save()

    st.success(
        f"Backup saved successfully!\n\n{file}"
    )