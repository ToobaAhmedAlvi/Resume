import streamlit as st
from PIL import Image
image = Image.open("logo.png")
st.image(image, width=125)
st.title("Job Category Prediction via CV Analysis")
html_temp = """
<div style="background:#025246 ;padding:10px">
<h2 style="color:white;text-align:center;"> CV Analysis NLP App </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)
