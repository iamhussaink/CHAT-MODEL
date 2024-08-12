import streamlit as st
import os
import random
from langchain_community.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')

template = """You are a chatbot having a conversation with a human.You are given with a conversation of Human and AI assistant. Behave as a 
AI assistant and answer the lastest question asked by human being by considering the previous conversation

{chat_history}
Human: {human_input}"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)



llm = GooglePalm(google_api_key=API_KEY)
chain = LLMChain(llm=llm, prompt=prompt)

greetings = [
    "Hello, how can I assist you today?",
    "Welcome, I'm here to help you with any questions or concerns.",
    "Good day, I'm your AI assistant, how can I help?",
    "Hi, I'm here to provide information and answer your questions.",
    "Greetings, I'm your virtual assistant, what can I help you with?",
]

chat_history = ""


greetings = random.choice(greetings)

st.title("💬 Chatbot")

#initial check
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": greetings}]

#for printing chat messages and creating a chat history 
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    if msg['role']=='user':
        chat_history += f"user:{msg['content']}\n\n"
    else:
        chat_history += f"assistant:{msg['content']}\n\n"


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = chain.invoke({"human_input": prompt, "chat_history": chat_history})
    response = response['text']
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

