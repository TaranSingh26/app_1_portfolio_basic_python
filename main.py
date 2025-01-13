import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/pic.jpg")

with col2:
    st.title("Tarandeep Singh")
    content = """
    
    Hi! Myself Tarandeep Singh, I am learning new things and this is my attempt at building a 
    basic portfolio website using python.
    
    """

    st.info(content)