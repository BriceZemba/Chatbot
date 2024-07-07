import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini-pro
model = genai.GenerativeModel("gemini-pro")

#Make an history
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title='Gemin-Chat-Model',
                   page_icon='🤖',
                   initial_sidebar_state='collapsed')

st.header('Gemini-chatbot-🤖')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key='input')

submit = st.button('Submit')

if submit and input :
    response = get_gemini_response(input)
    ##Add user query
    st.session_state['chat_history'].append(("You",input))
    st.subheader("the response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk))

st.subheader("The chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
                   