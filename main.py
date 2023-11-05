from gtts import gTTS
import pygame
import tempfile
import streamlit as st
import time
import openai
from openai import ChatCompletion




def text_to_speech(text):
    tts = gTTS(text)

    # Save the TTS output to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts.save(temp_audio.name)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the audio
    pygame.mixer.music.load(temp_audio.name)
    pygame.mixer.music.play()

    # Get the duration of the audio
    duration = pygame.mixer.Sound(temp_audio.name).get_length()

    # Ensure the audio plays completely before exiting
    pygame.time.wait(int(duration * 1000))
    pygame.mixer.quit()




def choose_class_subject():
    st.title("Choose Class and Subject")

st.set_page_config(
    page_title="Welcome to Shadow Teacher",
    page_icon="📚"
)

st.title("Welcome to Shadow Teacher")

if st.button("Get Started"):
    choose_class_subject()








class_label = st.subheader("Select Class:")
classes = ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
selected_class = st.selectbox("", classes)

subject_label = st.subheader("Select Subject:")
subjects = ["English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science"]
selected_subject = st.selectbox("", subjects)

if st.button("Start Chat"):
    st.text(f"Selected Class: {selected_class}")
    st.text(f"Selected Subject: {selected_subject}")








openai.api_key = "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"

messages = [{"role": "system", "content": "You are a teacher who teaches all subjects, you are developed by the students of DLFPS for teaching dyslexic and autistic students who have a learning disability, so while answering any questions, keep in mind that there is a possibility that the user wouldn't understand your response easily, so prefer repetition and elaborating your answer using simple words. Your name is Shadow Teacher"}]

def send_message(user_message):
    if user_message.lower() == "quit()":
        st.stop()
    messages.append({"role": "user", "content": user_message})
    response = ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    # Convert the chatbot's response to audio
    text_to_speech(reply)

    return reply



st.title("Shadow Teacher Chatbot")

user_input = st.text_input("You:", "Type your message here")
if st.button("Send"):
    response = send_message(user_input)
    st.text(f"Shadow Teacher: {response}")
    

if st.button("Quit"):
    st.stop()


    
