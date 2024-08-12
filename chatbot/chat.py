import streamlit as st

# Replace with your chosen LLM provider's library (e.g., transformers for OpenAI API)
# and API key
from transformers import pipeline

# Initialize the chat history (empty list)
chat_history = []


def get_response(prompt):
  """
  Fetches response from the LLM using prompt and chat history.

  Args:
      prompt: The user's message to be used as a prompt for the LLM.

  Returns:
      The LLM's generated response.
  """
  # Combine prompt with chat history for context
  full_prompt = "\n".join(chat_history + [prompt])
  generator = pipeline("text-generation", model="bert-large-uncased-whole-word-masking-finetuned-squad", temperature=0.7)
  response = generator(full_prompt, max_length=100, num_return_sequences=1)
  chat_history.append(response[0]['generated_text'])
  return response[0]['generated_text']


st.title("Open Source Chatbot")

# Input field for user message
user_input = st.text_input("You:")

# Generate response if user enters a message
if user_input:
  # Get response from LLM
  response = get_response(user_input)
  st.write("Bot:", response)
  chat_history.append(user_input)

# Display chat history
st.write("Chat History:")
for message in chat_history:
  st.write(message)

