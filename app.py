from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Geminni Pro model and get responses

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

## If submit button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)

