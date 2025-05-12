import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import pipeline
import streamlit as st
from HuggingFaceApp import summarize  # Your custom functions

# Define the options for the drop-down menu
st.title("Summerization of text app")
st.markdown("This app Summerizes your Text in real time!")
# Ask the user for input text
text = st.text_area("Enter your text here:")


# Run button
if st.button("Run"):
    st.subheader("Summary")
    result = summarize(text)
    st.write(result)


