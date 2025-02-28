import streamlit as st
from PIL import image

img = Image.open("background.jpeg")

st.image(

    img, caption = "start"
    width = 800,
    channels = "RGB"
)

# Header Text
st.markdown(
    "<h1 style='text-align: center; color: red; font-size: 36px; font-weight: bold;'>Memory App</h1>", 
    unsafe_allow_html=True
)