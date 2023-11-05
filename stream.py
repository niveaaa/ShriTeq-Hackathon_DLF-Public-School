import streamlit as st
import openai
from openai import ChatCompletion




def choose_class_subject():
    st.title("Choose Class and Subject")
    # Your code for the class and subject selection page goes here

st.set_page_config(
    page_title="Welcome to Shadow Teacher",
    page_icon="📚"
)

st.title("Welcome to Shadow Teacher")

# Create a "Get Started" button
if st.button("Get Started"):
    choose_class_subject()














#st.set_page_config(
#    page_title="Choose Class and Subject",
#    page_icon="📚"
#)




# Create a selectbox for class selection
class_label = st.subheader("Select Class:")
classes = ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
selected_class = st.selectbox("", classes)

# Create a selectbox for subject selection
subject_label = st.subheader("Select Subject:")
subjects = ["English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science"]
selected_subject = st.selectbox("", subjects)

# Create a "Start Chat" button
if st.button("Start Chat"):
    st.text(f"Selected Class: {selected_class}")
    st.text(f"Selected Subject: {selected_subject}")
    # You can launch your chat interface here with the selected class and subject















# Set your OpenAI API key
openai.api_key = "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"

# Create an initial message for the chatbot
messages = [{"role": "system", "content": "You are a teacher who teaches all subjects, you are developed by the students of DLFPS for teaching dyslexic and autistic students who have a learning disability, so while answering any questions, keep in mind that there is a possibility that the user wouldn't understand your response easily, so prefer repetition and elaborating your answer using simple words. Your name is Shadow Teacher"}]

# Create a function to send a user message to the chatbot and get a response
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
    return reply


# Create a Streamlit app

# st.set_page_config(page_title="Shadow Teacher Chatbot", page_icon="🤖")


st.title("Shadow Teacher Chatbot")

user_input = st.text_input("You:", "Type your message here")
if st.button("Send"):
    response = send_message(user_input)
    st.text(f"Shadow Teacher: {response}")  # Corrected line

# Add an option to quit the chat
if st.button("Quit"):
    st.stop()
