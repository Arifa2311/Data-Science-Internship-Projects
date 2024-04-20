import streamlit as st
import google.generativeai as genai

# Improved intro message
intro_message = """
Hi there! 👋 I'm Chitti The Robot , your AI Data Science Assistant. I'm here to assist you with all things data science! Whether you need help understanding algorithms, analyzing data, or coding in Python, I've got you covered. Feel free to ask me anything related to data science, and I'll do my best to provide you with accurate and helpful answers. Let's dive into the world of data together! 🚀
"""

# Title styling
st.markdown(
    """
    <style>
        .title-text {
            color: #008080; /* Dark cyan */
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            padding: 20px;
        }
        .subtitle-text {
            color: #4B0082; /* Indigo */
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            padding: 10px;
        }
    </style>
    """
    , unsafe_allow_html=True
)

# Title and subtitle
st.markdown('<p class="title-text">🌟 Welcome to Chitti Robot - Your Data Science Assistant 🌟</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">🤖 Chitti Robot is Ready to Assist You! 🤖</p>', unsafe_allow_html=True)

# Load API key from file
with open(r"C:\Users\Afrin\Downloads\Conversation_AI\Genai API Key.txt") as f:
    api_key = f.read()

# Configure GenerativeAI
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction=intro_message
)

# Initialize chat history if not already present
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Start chat with the AI model
chat = model.start_chat(history=[])

st.chat_message("AI-chitti the robot").write("Hi there! 👋 How can I help you today? 😊")

for message in chat.history:
    sender = "AI-chittirobot" if message.role == "model" else message.role
    st.chat_message(sender).write(message.parts[0].text)

user_input = st.chat_input()

if user_input:
    st.chat_message("user👤").write(user_input)
    response = chat.send_message(user_input)
    for bot in response:
        st.chat_message("AI-chittirobot🤖").write(bot.text)
    st.session_state["memory"] = chat.history
