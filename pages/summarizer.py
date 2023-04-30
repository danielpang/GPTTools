import streamlit as st
from dotenv import load_dotenv

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')
st.set_page_config(
    page_title="Article/ Text Summarizer",
    page_icon=":robot_face",
    initial_sidebar_state="expanded",
    layout="wide",
)

st.write("# Text/ Article Summarizer")
st.write("### Enter text to summarize in a sentence/ multiple points.")

def get_prompt(text):
    return f"""
        Your task is to summarize the following text, delimited by triple backticks, into at most three\
        points.\ 

        Text: ```{text}```
        """

def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_user_input():
    text_to_summarize = st.text_area("Text to summarize")
    return text_to_summarize

text_to_summarize = get_user_input()
if text_to_summarize:
    prompt = get_prompt(text_to_summarize)
    response = get_completion(prompt)
    st.text(response)