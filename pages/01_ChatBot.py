from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 

groq_api_key=st.secrets["GROQ_API_KEY"]

model=ChatGroq(model="Llama-3.3-70b-Versatile", groq_api_key=groq_api_key)
parser=StrOutputParser()

# prompt template 
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question: {Question}")   
    ]
)

# streamlit app 

st.title("Chatbot using Groq and Llama 3.3-70b")
input_text=st.text_input("What question do you have in mind")



chain=prompt|model|parser

if input_text.strip() == "":
    st.error("Please enter any question")
else:
    try:
        with st.spinner("Your response is being generated....."):
            response=chain.invoke({"Question":input_text})
            with st.container(border=True):
                st.write(response)
    except Exception as e:
            st.error(f"An error occured: {e}")