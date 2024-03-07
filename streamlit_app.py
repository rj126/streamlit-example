import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from openai import OpenAI

# Title
st.title("Name Matching App")

# User input for two names
name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

# Button to check for match (without any action)
if st.button("Check for Match"):
    pass
