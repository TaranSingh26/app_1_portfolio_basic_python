import streamlit as st
import pandas

st.set_page_config(layout="wide")
col_1, col_2 = st.columns(2)

with col_1:
    st.image("images/pic.jpg")

with col_2:
    st.title("Tarandeep Singh")
    content = """
    
    Hi! Myself Tarandeep Singh, I am learning new things and this is my attempt at building a 
    basic portfolio website using python.
    
    """

    st.info(content)

content_2 = """

Below are some projects I am currently working on.

"""

st.text(content_2)

col_3, empty_col, col_4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col_3:

    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col_4:

    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")