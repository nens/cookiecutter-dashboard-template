import streamlit as st

second_page = st.Page("second_page.py", title="Tweede pagina")

home_page = st.navigation([second_page])

st.set_page_config(page_title="{{ cookiecutter.project_name }}")
st.write("Reinout is geweldig!")
home_page.run()
