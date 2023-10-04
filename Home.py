import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Savan Patel", page_icon="images/favicon.ico", layout="wide")

col1, col2 = st.columns(2)

with col1:
    profile_pic = Image.open("images/photo.jpg")
    rotated_profile_pic = profile_pic.rotate(0, expand=True)
    st.image(rotated_profile_pic, width=300)

with col2:
    st.title("Savan Patel")
    content = """Welcome to my website! I am a computer programmer with expertise in Python programming and C++, 
    and a full stack web developer. Currently, I work as a project manager, and I have extensive experience in 
    managing large-scale projects. My expertise in project management has allowed me to ensure that projects are 
    completed on time and within budget, while also ensuring that they meet the needs of stakeholders."""
    st.info(content)

content_2 = """
Below are some of the projects that I have worked on. Click on the links to learn more about them.
"""

st.markdown(content_2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:(int(len(df)/2))].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"], width=300)
        st.write(row["description"])
        st.write("[Source Code](" + row["url"] + ")")

with col4:
    for index, row in df[(int(len(df)/2)):].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"], width=300)
        st.write(row["description"])
        st.write("[Source Code](" + row["url"] + ")")
