from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st 

groq_api_key=st.secrets["GROQ_API_KEY"]

model=ChatGroq(model="Llama-3.3-70b-Versatile", groq_api_key=groq_api_key)
parser=StrOutputParser()


# streamlit app
st.title("Language Translation App")
st.write("This app uses the Groq and Meta's AI model to translate text into different languages.")

input_language=st.selectbox("Select a language",("Hindi", "Telugu", "Kannada","Tamil", "Malayalam", "Marathi","French", "Spanish", "Japanese", "Chinese"))
input_text=st.text_input("Enter the text to be translated")


# Translation button
if st.button("Translate"):
    if input_text.strip() == "":
        st.error("Please enter some text to translate.")
    else:
        # Define the prompt template
        generic_template = "Translate the following into {input_language}"
        prompt = ChatPromptTemplate.from_messages(
            [("system", generic_template), ("user", "{input_text}")]
        )

        # Create the chain and invoke it
        chain1 = prompt | model | parser
        with st.spinner("Text is being translated....."):
            output_text = chain1.invoke({"input_language": input_language, "input_text": input_text})
        
        # Display the output
        st.write("Translated Text:")
        with st.container(border=True):
            st.write(output_text)