
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBWAhYYQ4n89Qgu2N0ae6g-mpDIlbIRiuk")
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("Gemini Chatbot")
user_input = st.text_input("Ask me anything:")
if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)

# streamlit run Chatbot.py
