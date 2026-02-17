from pathlib import Path

import streamlit as st

st.set_page_config(page_title="{{ cookiecutter.project_name }}")
st.markdown(Path("README.md").read_text())
