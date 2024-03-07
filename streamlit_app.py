import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["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""])
ASST_PROMPT = "I need help making a decision."

# Title
st.title("Name Matching App")

# User input for two names
name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

# Button to check for match (without any action)
if st.button("Check for a Match"):
    pass
