import streamlit as st
import os
from langchain_community.llms import GooglePalm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

# Replace with your Google Generative AI API key
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ.get('API_KEY')

# Define the chat prompt template
template = """You are a helpful assistant. Please respond to the user's question: {input}"""
prompt = PromptTemplate(
    input_variables=[ "input"], template=template
)

# Initialize the GooglePalm language model
llm = GooglePalm(google_api_key=API_KEY)

chain = LLMChain(prompt=prompt, llm=llm)

# Create a Streamlit app
st.title("Ask me anything")
# Get user input
input_text =  st.text_input("Enter the Query ")
if input_text:
    st.header(f"Query: {input_text}")
    with st.spinner("Loading..."):
        response = chain.predict(input=input_text)
        st.write(response)
