import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

"""
# OpenAI API key
openai.api_key = "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"
"""

# Title
st.title("Name Matching App")

# User input for two names
name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

# Button to check for match (without any action)
if st.button("Check for Match"):
    pass
