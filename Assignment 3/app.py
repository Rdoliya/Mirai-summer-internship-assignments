import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# =====================================
# Load Environment Variables
# =====================================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found.")
    st.stop()

client = genai.Client(api_key=API_KEY)

# =====================================
# Page Config
# =====================================
st.set_page_config(
    page_title="Memory Vault Chatbot",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Memory Vault Chatbot")
st.write(
    "A stateful AI chatbot powered by Streamlit Session State and Google Gemini."
)

# =====================================
# Personalities
# =====================================
personalities = {
    "🤵 Common Indian Man": "Talk like a friendly common Indian man.",
    "💪 Crazy Salman Khan Fan": "You absolutely love Salman Khan.",
    "👦 Little Boy": "You are a curious 7-year-old child.",
    "🔥 Motivational Coach": "Speak like a motivational speaker.",
    "💻 Software Engineer": "Explain technical concepts clearly.",
    "👨‍🏫 College Professor": "Teach concepts in detail.",
    "😂 Stand-up Comedian": "Always include humor.",
    "🚀 Entrepreneur": "Think like a startup founder.",
    "📚 Friendly Teacher": "Teach patiently and simply.",
    "🤖 AI Assistant": "Professional helpful AI assistant."
}

selected = st.sidebar.selectbox(
    "Choose Personality",
    list(personalities.keys())
)

# =====================================
# Memory Vault
# =====================================
if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}

if selected not in st.session_state.all_chats:
    st.session_state.all_chats[selected] = []

messages = st.session_state.all_chats[selected]

# =====================================
# Clear Chat
# =====================================
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.all_chats[selected] = []
    st.rerun()

# =====================================
# Render Chat History
# =====================================
for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================================
# Chat Input
# =====================================
if prompt := st.chat_input("Say something..."):

    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    system_prompt = f"""
You are {selected}

Instructions:
{personalities[selected]}

Stay in character.
Be natural.
Be conversational.
"""

    with st.spinner("Thinking..."):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{system_prompt}\n\nUser: {prompt}"
            )

            answer = response.text

        except Exception as e:
            answer = str(e)

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)