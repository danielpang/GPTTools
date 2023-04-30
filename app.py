import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="GPT Tools",
        page_icon=":robot_face",
    )

    st.write("# GPT Tools")
    st.write("### Collection of productivity tools for work or personal use")

if __name__ == "__main__":
    run()    