import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import pipeline
import streamlit as st
from HuggingFaceApp import  translate  # Your custom functions

st.title("Translation of text app")
st.markdown("This app Translates your Text in real time!")

# Ask the user for input text
text = st.text_area("Enter your text here:")

# Extra input for Translation
language = ""
language = st.text_input("Enter target language (e.g., French, German):")

# Run button
if st.button("Run"):
    if language.strip():
        st.subheader("Translation")
        result = translate(text, language)
        st.write(result)
    else:
        st.warning("Please enter a target language.")



