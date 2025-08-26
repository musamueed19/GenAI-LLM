from langchain_ollama import ChatOllama
import streamlit as st

from langchain.prompts import PromptTemplate

promptTemplate = PromptTemplate(
    input_variables=["country", "language"],
    template="""
    You are an expert in traditional cuisines.
    You provide me information about specific dish from a specific country.
    Answer the question: What is the traditional cuisine of the {country}?
    Answer in {language} words
    """
)

llm = ChatOllama(model='gemma:2b')

st.title("Traditional Cuisines")
country = st.text_input("Enter Country Name")
language = st.selectbox(label="language", options=["english", "urdu", "arabic", "hindi", "chinese", "french", "german"])

if country and language:
    response = llm.invoke(promptTemplate.format(country=country, language=language))
    st.write(response.content)