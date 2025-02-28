import streamlit as st
import base64

# Use @st.cache_data instead of @st.experimental_memo
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get the base64-encoded image
img = get_img_as_base64("background.jpeg")

# Custom CSS for Background Image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Header Text
st.markdown(
    "<h1 style='text-align: center; color: red; font-size: 36px; font-weight: bold;'>Memory App</h1>", 
    unsafe_allow_html=True
)