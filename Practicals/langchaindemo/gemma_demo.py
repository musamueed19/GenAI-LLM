import os

# from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama


llm = ChatOllama(model="gemma:2b")

question = input("Hi👋🏻! I am Dartrex. You can ask me any question?\n")

response = llm.invoke(question)
print(response.content)