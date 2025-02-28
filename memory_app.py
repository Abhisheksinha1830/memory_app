import streamlit as st
import base64

# Custom CSS for Background Image
@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("background.jpg")

page_bg_img = f"""
<style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
# background-size: 180%;
# background-position: top left;
# background-repeat: no-repeat;
# background-attachment: local;
# }}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("background.png");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Header Text
st.markdown(
    "<h1 style='text-align: center; color: red; font-size: 36px; font-weight: bold;'>Memory App</h1>", 
    unsafe_allow_html=True
)