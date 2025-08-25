import os

from langchain_openai import ChatOpenAI

# OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

question = input("Hi! I am Dartrex. You can ask me any question?")

response = llm.invoke(question)
print(response.content)
