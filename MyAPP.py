
# import os
# os.environ["TRANSFORMERS_NO_TF"] = "1"

# from transformers import pipeline

# import streamlit as st
# import transformers
# from HuggingFaceApp import translate, mask, summarize  # Assuming these are your own wrapper functions

# # Define the options for the drop-down menu
# options = ["Summarization", "Masking", "Translation"]

# # Create the drop-down menu
# selected_option = st.selectbox("Choose an option:", options)

# # Ask the user for input text
# text = st.text_area("Enter your text here:")

# # Process based on selected option
# if st.button("Run",key="1"):
#     if selected_option == "Summarization":
#         st.subheader("Summary")
#         result = summarize(text)
#         st.write(result)

#     elif selected_option == "Masking":
#         predictions = mask(text)
#         for result in predictions:
#             st.write(result)


#     elif selected_option == "Translation":
#         language = st.text_input("Enter target language (e.g., French, German):")
#         if st.button("Run",key="2"):
#             result = translate(text, language)
#             st.subheader("Translation")
#             st.write(result)
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import pipeline
import streamlit as st
from HuggingFaceApp import translate, mask, summarize  # Your custom functions

# Define the options for the drop-down menu
options = ["Summarization", "Masking", "Translation"]

# Create the drop-down menu
selected_option = st.selectbox("Choose an option:", options)

# Ask the user for input text
text = st.text_area("Enter your text here:")

# Extra input for Translation
language = ""
if selected_option == "Translation":
    language = st.text_input("Enter target language (e.g., French, German):")

# Run button
if st.button("Run"):
    if selected_option == "Summarization":
        st.subheader("Summary")
        result = summarize(text)
        st.write(result)

    elif selected_option == "Masking":
        st.subheader("Masked Output")
        predictions = mask(text)
        for result in predictions:
            st.write(result)

    elif selected_option == "Translation":
        if language.strip():
            st.subheader("Translation")
            result = translate(text, language)
            st.write(result)
        else:
            st.warning("Please enter a target language.")



