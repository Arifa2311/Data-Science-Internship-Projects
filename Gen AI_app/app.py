import streamlit as st
from openai import OpenAI

st.title("GenAI App - AI Code Reviewer")

# Read API key from file
with open(r"C:\Users\Afrin\Downloads\Internship work\Gen AI_app\Keys\.open_api_key.txt") as f:
    key = f.read().strip()

# Initialize OpenAI client with API key
client = OpenAI(api_key=key)

# Input field for Python code
prompt = st.text_area("Enter your Python code... 🐍")

if st.button("Generate"):
    st.spinner("Please wait...")

    # Perform code review using OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Give the bugs is exists in the code with a side heading and Give the correct code for the given code"},
            {"role": "user", "content": prompt}
        ]
    )

    st.header("Review of your code:")
    st.write(response.choices[0].message.content)
