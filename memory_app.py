import streamlit as st

# Custom CSS for Background Image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("background.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Text
st.markdown(
    "<h1 style='text-align: center; color: pink;'>Memory App</h1>", 
    unsafe_allow_html=True
)