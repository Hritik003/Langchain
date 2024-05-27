from langchain_openai import  OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

def get_openai_response(question):
    llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm.invoke([{"role": "user", "content": question}])
    return response

st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_openai_response(input_text)
    # print(response)
    st.subheader("The response is:")
    st.write(response)
