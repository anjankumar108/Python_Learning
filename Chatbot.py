import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

API_KEY = os.getenv("GOOGLE_API_KEY")
        


import streamlit as st
import google.generativeai as genai

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("Gemini Chatbot")
user_input = st.text_input("Ask me anything:")
if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)

# streamlit run Chatbot.py
