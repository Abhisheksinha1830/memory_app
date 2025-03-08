import streamlit as st
from PIL import Image  # Changed 'image' to 'Image'

img1 = Image.open("sad_puppy.jpg")
img2 = Image.open("heart.jpeg")
img3 = Image.open("flowers.jpg")
img4 = Image.open("special_photo.jpeg")

# st.image(Image.open("background.jpeg"))

# st.image(
#     img, caption="start",
#     width=800,
#     channels="RGB"
# )

# # Header Text
# st.markdown(
#     "<h1 style='text-align: center; color: red; font-size: 36px; font-weight: bold;'>Memory App</h1>", 
#     unsafe_allow_html=True
# )

import streamlit as st

st.title("I'm Sorry, My Ven 💖")
st.write("I'm so sorry for talking rudely. Answer few question and there's a surprise for you!")

# Initialize session state
if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0

total_questions = 3

# Question 1
if st.session_state.quiz_step == 0:
    st.subheader("What will I do to make things better?")
    st.image(img1, caption="I'm so sorry! 😢", width=400)
    q1_answer = st.radio(
        "Choose an answer:",
        ["Listen to you more", "Buy you a treat", "Give you a kiss"],
        key="q1"
    )
    if st.button("Submit Answer"):
        if q1_answer == "Listen to you more":
            st.success("You're right! I promise to be better.")
        if q1_answer == "Buy you a treat":
            st.success("Done! We can order something online")
        if q1_answer == "Give you a kiss":
            st.success("Xoxo 😘")                        
        st.session_state.quiz_step += 1
        # Add "Start Again" button to restart the quiz
    if st.button("Next"):
        st.session_state.quiz_step = 1  # Reset to the first question

# Question 2
elif st.session_state.quiz_step == 1:
    st.subheader("What do I love most about you?")
    st.image(img2, caption="You mean the world to me! 💕", width=400)
    q2_answer = st.radio(
        "Choose an answer:",
        ["Your laugh", "The way you love me", "Whole Package"],
        key="q2"
    )
    if st.button("Submit Answer"):
        if q2_answer == "Your laugh":
            st.success("Exactly! Your laugh makes me so happy.")
        if q2_answer == "The way you love me":
            st.success("I love the way you care about me babe. Love you!")
        if q2_answer == "Whole Package":
            st.success("Damn! You are amazingly HOTTTT.")
        st.session_state.quiz_step += 1
    if st.button("Back"):
        st.session_state.quiz_step = 0  # Reset to the first question
    if st.button("Next"):
        st.session_state.quiz_step = 2  # Reset to the first question
# Question 3
elif st.session_state.quiz_step == 2:
    st.subheader("Question 3: How will I make it up to you?")
    st.image(img3, caption="I want to make you happy! 🌸", width=400)
    q3_answer = st.radio(
        "Choose an answer:",
        ["Plan a special date", "Forget about it", "Argue more"],
        key="q3"
    )
    if st.button("Submit Answer"):
        if q3_answer == "Plan a special date":
            st.success("Yes! This trip I PROMISE I’ll plan something special to show you how much you mean to me.")
        if q3_answer == "Forget about it":
            st.success("No babe, I am sorry.")
        if q3_answer == "Argue more":
            st.success("Wrong Option baby")                        
        st.session_state.quiz_step += 1
    if st.button("Back"):
        st.session_state.quiz_step = 1  # Reset to the first question
    # if st.button("Next"):
    #     st.session_state.quiz_step = 0  # Reset to the first question
# Reward
else:
    st.write("Quiz Complete! You've unlocked a special message!")
    if st.button("Reveal Your Reward"):
        st.image(img4, caption="I’m so sorry, and I love you so much! 💕", width=600)
        st.balloons()
    # Add "Start Again" button to restart the quiz
    if st.button("Start Again"):
        st.session_state.quiz_step = 0  # Reset to the first question
