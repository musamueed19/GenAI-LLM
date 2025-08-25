from langchain_ollama import ChatOllama


llm = ChatOllama(model="mistral")

question = input("Hi👋🏻! I am Dartrex. You can ask me any question?\n")

response = llm.invoke(question)
print(response.content)