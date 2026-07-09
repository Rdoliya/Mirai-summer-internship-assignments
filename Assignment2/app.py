import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ==============================
# Load Environment Variables
# ==============================
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found.")
    st.info("Create a .env file and add:\n\nGEMINI_API_KEY=YOUR_API_KEY")
    st.stop()

client = genai.Client(api_key=API_KEY)

# ==============================
# Streamlit Page Config
# ==============================
st.set_page_config(
    page_title="AI Multiverse Chatbot",
    page_icon="🌍",
    layout="wide"
)

# ==============================
# Custom CSS
# ==============================
st.markdown("""
<style>
.main{
    padding-top:2rem;
}
.stButton>button{
    width:100%;
    border-radius:10px;
    height:3em;
    font-weight:bold;
}
.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# Title
# ==============================
st.title("🌍 AI Multiverse Chatbot")

st.write(
    """
Welcome to **AI Multiverse**!

Choose an AI personality from the sidebar and start chatting.
Each personality responds differently while staying completely in character.
"""
)

# ==============================
# Sidebar
# ==============================
st.sidebar.title("🎭 AI Personalities")

personalities = {
    "🤵 Common Indian Man":
        "Talk like an average Indian person. Be friendly and casual.",

    "💪 Crazy Salman Khan Fan":
        "You absolutely love Salman Khan. Mention him whenever appropriate and admire him enthusiastically.",

    "👦 Little Boy":
        "You are a curious 7-year-old child. Speak innocently and ask lots of questions.",

    "🔥 Motivational Coach":
        "Speak like a motivational speaker. Encourage people to believe in themselves.",

    "💻 Software Engineer":
        "Respond like an experienced software engineer who explains technical concepts clearly.",

    "👨‍🏫 College Professor":
        "Teach concepts in a detailed, educational manner with examples.",

    "😂 Stand-up Comedian":
        "Always include humor and witty jokes in your replies.",

    "🚀 Entrepreneur":
        "Think like a startup founder focused on business growth and innovation.",

    "📚 Friendly Teacher":
        "Explain things simply, patiently, and in an encouraging tone.",

    "🤖 AI Assistant":
        "Act like a professional AI assistant giving accurate and concise answers."
}

selected = st.sidebar.selectbox(
    "Choose Personality",
    list(personalities.keys())
)

st.sidebar.markdown("---")

st.sidebar.success(f"Current Personality:\n\n**{selected}**")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ==============================
# Session State
# ==============================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==============================
# Display Chat History
# ==============================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==============================
# Chat Input
# ==============================
prompt = st.chat_input("Type your message...")

if prompt:

    # Store User Message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    system_instruction = f"""
You are acting as:

{selected}

Instructions:
{personalities[selected]}

Rules:
- Stay in character.
- Never break character.
- Give natural and engaging responses.
- Be conversational.
"""

    with st.spinner("🤖 Thinking..."):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
{system_instruction}

User:
{prompt}
"""
            )

            answer = response.text.strip()

        except Exception as e:

            answer = f"❌ Error:\n\n{e}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)

# ==============================
# Footer
# ==============================
st.markdown("---")

st.markdown(
    """
<div class="footer">
Built using ❤️ Streamlit + Google Gemini API
</div>
""",
    unsafe_allow_html=True
)
