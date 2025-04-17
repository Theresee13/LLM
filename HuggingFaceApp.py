#!/usr/bin/env python
# coding: utf-8

# ## Summarization

# In[20]:

import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")


# In[22]:


def summarize(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]["summary_text"]


# ## Masking

# In[29]:


from transformers import pipeline
unmasker = pipeline("fill-mask", model="bert-base-uncased", framework="pt", device=-1)



# In[31]:


def mask(text):
    predictions = unmasker(text)
    formatted = []
    for pred in predictions:
        formatted.append(f"{pred['token_str']} (score: {pred['score']:.4f})")
    return formatted

    


# ## Translation

# In[47]:


from transformers import T5Tokenizer, T5ForConditionalGeneration
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Load model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")
def translate(text, language):
    sentences = sent_tokenize(text)
    translated_chunks = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence.endswith("."):
            sentence += "."  # Add a period if it's missing
        prompt = f"translate English to {language.capitalize()}: {sentence}"
        input_ids = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).input_ids
        output_ids = model.generate(input_ids, max_length=512)
        translated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        translated_chunks.append(translated_text)

    full_translation = " ".join(translated_chunks)
    return full_translation


