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

# Title
st.title("Name Matching App")

# User input for two names
name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

# Display the entered names
st.write("You entered the following names:")
st.write(f"Name 1: {name1}")
st.write(f"Name 2: {name2}")

"""
# Button to trigger the request
if st.button("Match Names"):
    # Send request to OpenAI assistant
    response = openai.Completion.create(
        engine="asst_qLeO39Rs0DI6XxZGON3hOiNL",
        prompt=f"Match the names '{name1}' and '{name2}'.",
        max_tokens=50,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )
    # Display the response
    st.write("OpenAI Response:")
    st.write(response.choices[0].text.strip())
"""

