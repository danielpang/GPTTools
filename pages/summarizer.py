import streamlit as st
from dotenv import load_dotenv

import openai
import os
import validators

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
st.write("### Enter text or url of article to summarize into multiple points.")

def get_prompt(text):
    return f"""
        Your task is to summarize the following text, delimited by triple backticks, into at most five\
        points.\

        Display the output in the form of bullet points like
        - Point 1
        - Point 2
        - Point 3

        Text: ```{text}```
        """

def get_webpage_prompt(url):
    return f"""
        Your task is to generate a summary of a web article \
        from a link.

        Summarize the web article from the link, delimited by triple \
        backticks, in five points or less. \

        Display the output in the form of bullet points like
        - Point 1
        - Point 2
        - Point 3

        Web article: ```{url}```
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
    user_input = st.text_area("Text or article to summarize")
    return user_input

def is_url(str):
    return validators.url(str)

user_input = get_user_input()
if user_input:
    if is_url(user_input):
        prompt = get_webpage_prompt(user_input)
    else:
        prompt = get_prompt(user_input)
    response = get_completion(prompt)
    st.text(response)