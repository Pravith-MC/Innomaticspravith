import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyANXKToNQAiMjS4BjrES0vTf72h1IG-qe4')
sys_prom ="""Imagine yourselve as a code reviewer for all the programming languages.If there are any mistakes entered by the user
             please correct it.Give them the new and correct code for it."""
model = genai.GenerativeModel(model_name ="models/gemini-1.5-flash-latest",system_instruction=sys_prom)
st.title("AI Code Reviewer Bot")
user_prom = st.text_input("Enter your query: ",placeholder="Type your question here")
bt_click = st.button("Generate Answer")

if bt_click == True:
    response = model.generate_content(user_prom)
    st.write(response.text)