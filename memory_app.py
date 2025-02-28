import streamlit as st
import base64
import os

@st.cache_data
def get_img_as_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"Could not find image file: {file}. Using a default background instead.")
        return None

# Get the absolute path to the image
file_path = "https://images.unsplash.com/photo-1501426026826-31c667bdf23d"
print(f"Checking if file exists at: {file_path}")
if not os.path.exists(file_path):
    st.error(f"File not found at {file_path}. Check the path or file name.")
    img = None
else:
    img = get_img_as_base64(file_path)

# Custom CSS for Background Image
if img:
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/jpeg;base64,{img}");
        background-size: 180%;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/jpeg;base64,{img}");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
else:
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
        background-size: 180%;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }

    [data-testid="stSidebar"] > div:first-child {
        background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """

st.markdown(page_bg_img, unsafe_allow_html=True)

# Header Text
st.markdown(
    "<h1 style='text-align: center; color: red; font-size: 36px; font-weight: bold;'>Memory App</h1>", 
    unsafe_allow_html=True
)