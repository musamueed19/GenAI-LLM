from langchain_ollama import ChatOllama

import streamlit as st

llm = ChatOllama(model='gemma:2b')

st.title("Hi 👋🏻, I'm CAPT. MUSA")
question = st.text_input("You can ask me anything...")

if question:
    response = llm.invoke(question)
    st.write(response.content)