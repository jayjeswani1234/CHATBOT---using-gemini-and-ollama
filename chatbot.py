import streamlit as st
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load env
load_dotenv()

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("user", "Question: {question}")
    ]
)

# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
# Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# UI
st.title("AI Chatbot")

input_text = st.text_input("Ask something")

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)