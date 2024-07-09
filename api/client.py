import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
                           json={'input':{'topic':input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={'input':{'topic':input_text}})   
    return response.json()['output']

## Streamlit Framework

st.title('Langchain Demo with openai and llama3 api')
input_text_essay = st.text_input('Write an essay on')
input_text_poem = st.text_input('Write a poem on')

if input_text_essay:
    st.write(get_openai_response(input_text_essay))

if input_text_poem:
    st.write(get_ollama_response(input_text_poem))