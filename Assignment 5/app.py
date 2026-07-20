import streamlit as st
from google import genai
from dotenv import load_dotenv
import requests
import json
import random
import os
import tempfile
from gtts import gTTS
from PIL import Image
from io import BytesIO
import urllib.parse

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="🎮 Multi-Modal Visual Novel",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 AI Multi-Modal Visual Novel")
st.caption(
    "Choose your adventure with AI-generated stories, images, and narration."
)

# ==========================================
# Cache Gemini Client
# ==========================================

@st.cache_resource
def load_client():
    return genai.Client(api_key=API_KEY)

if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found.")
    st.stop()

client = load_client()

# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("⚙ Story Settings")

genre = st.sidebar.selectbox(
    "Story Genre",
    [
        "Fantasy",
        "Science Fiction",
        "Mystery",
        "Adventure",
        "Horror",
        "Cyberpunk",
        "Romance",
        "Historical"
    ]
)

art_style = st.sidebar.selectbox(
    "Art Style",
    [
        "Anime",
        "Realistic",
        "Fantasy Art",
        "Oil Painting",
        "Watercolor",
        "3D Render",
        "Pixel Art",
        "Sketch"
    ]
)

if st.sidebar.button("🔄 Restart Story"):

    for key in [
        "history",
        "current_story",
        "current_image",
        "current_options",
        "chat"
    ]:
        if key in st.session_state:
            del st.session_state[key]

    st.rerun()

# ==========================================
# Session State
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []

if "current_story" not in st.session_state:
    st.session_state.current_story = ""

if "current_image" not in st.session_state:
    st.session_state.current_image = None

if "current_options" not in st.session_state:
    st.session_state.current_options = []

if "chat" not in st.session_state:
    st.session_state.chat = []

# ==========================================
# JSON Prompt
# ==========================================

SYSTEM_PROMPT = f"""
You are an interactive visual novel engine.

Story Genre:
{genre}

Return ONLY valid JSON.

Never return markdown.

Format:

{{
    "story_text":"A detailed story paragraph",

    "image_prompt":"Detailed image prompt in {art_style} style",

    "options":[
        "Option 1",
        "Option 2",
        "Option 3"
    ]
}}
"""

# ==========================================
# Generate Story
# ==========================================
def generate_story(user_choice):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
{SYSTEM_PROMPT}

Story History:

{json.dumps(st.session_state.history, indent=2)}

Player Choice:

{user_choice}

Return ONLY valid JSON.
Do not use markdown.
Do not wrap the JSON inside ``` blocks.
"""
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        data = json.loads(text)

        return data

    except json.JSONDecodeError:

        st.error("Gemini returned invalid JSON.")

        return None

    except Exception as e:

        st.error(f"Gemini Error: {e}")

        return None

# ==========================================
# Generate Image
# ==========================================

def generate_image(image_prompt):

    try:

        encoded_prompt = urllib.parse.quote(image_prompt)

        url = (
            f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            "?width=768&height=768"
        )

        response = requests.get(url, timeout=60)

        response.raise_for_status()

        return response.content

    except Exception:

        st.toast("🖼️ Image server is busy, skipping visual...")

        return None


# ==========================================
# Generate Narration
# ==========================================

def generate_audio(story):

    try:

        tts = gTTS(text=story, lang="en")

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        tts.save(temp_file.name)

        return temp_file.name

    except Exception:

        st.toast("🔊 Unable to generate narration.")

        return None


# ==========================================
# Display Story Scene
# ==========================================

def render_scene():

    if st.session_state.current_story == "":
        return

    st.subheader("📖 Story")

    st.write(st.session_state.current_story)

    if st.session_state.current_image:

        try:

            image = Image.open(
                BytesIO(st.session_state.current_image)
            )

            st.image(
                image,
                use_container_width=True
            )

        except Exception:
            pass

    audio = generate_audio(
        st.session_state.current_story
    )

    if audio:

        st.audio(audio)

    st.markdown("---")

    st.subheader("🎮 Choose Your Next Action")

    for i, option in enumerate(st.session_state.current_options):

        if st.button(option, key=f"option_{i}"):

            with st.spinner("Writing next chapter..."):
                story = generate_story(option)

            if story:

                st.session_state.current_story = story["story_text"]

                st.session_state.current_options = story["options"]

                st.session_state.history.append(
                    {
                        "user": option,
                        "story": story["story_text"]
                    }
                )

                st.session_state.current_image = generate_image(
                    story["image_prompt"]
                )

                st.rerun()


# ==========================================
# Start Story
# ==========================================

if st.session_state.current_story == "":

    st.subheader("🎬 Begin Your Adventure")

    opening = st.text_input(
        "Enter your character or opening idea",
        placeholder="Example: A young wizard searching for an ancient relic..."
    )

    if st.button("🚀 Start Story"):

        if opening.strip() == "":

            st.warning("Please enter a starting prompt.")

        else:

            with st.spinner("Creating your adventure..."):
                story = generate_story(opening)

            if story:

                st.session_state.current_story = story["story_text"]

                st.session_state.current_options = story["options"]

                st.session_state.history.append(
                    {
                        "user": opening,
                        "story": story["story_text"]
                    }
                )

                st.session_state.current_image = generate_image(
                    story["image_prompt"]
                )

                st.rerun()

else:

    render_scene()


# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.caption(
    "🎮 Multi-Modal Visual Novel • Powered by Google Gemini, Pollinations AI & Streamlit"
)

