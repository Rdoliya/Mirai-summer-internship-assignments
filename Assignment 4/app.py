import streamlit as st
import requests
import random
import urllib.parse

# ======================================
# Page Configuration
# ======================================

st.set_page_config(
    page_title="🎨 AI Image Studio",
    page_icon="🎨",
    layout="wide"
)

# ======================================
# Title
# ======================================

st.title("🎨 AI Image Studio")

st.write(
    "Generate stunning AI images using **Pollinations AI**."
)

# ======================================
# Sidebar
# ======================================

st.sidebar.header("⚙️ Generation Settings")

art_style = st.sidebar.selectbox(
    "Choose Art Style",
    [
        "Realistic",
        "Anime",
        "Fantasy",
        "Cyberpunk",
        "Pixel Art",
        "Oil Painting",
        "Watercolor",
        "3D Render",
        "Sketch",
        "Digital Art"
    ]
)

width = st.sidebar.slider(
    "Width",
    min_value=256,
    max_value=1024,
    value=512,
    step=64
)

height = st.sidebar.slider(
    "Height",
    min_value=256,
    max_value=1024,
    value=512,
    step=64
)

magic_enhance = st.sidebar.checkbox(
    "✨ Enable Magic Enhance"
)

# ======================================
# Prompt
# ======================================

prompt = st.text_area(
    "Describe your image",
    placeholder="Example: A futuristic city floating above the clouds..."
)

# ======================================
# Surprise Prompts
# ======================================

surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A giant panda working as a software engineer",
    "A dragon reading books inside a magical library",
    "An underwater palace built entirely from crystal"
]

# ======================================
# Buttons
# ======================================

col1, col2 = st.columns(2)

generate = col1.button("🎨 Generate Image")

surprise = col2.button("🎲 Surprise Me!")

# ======================================
# Decide Prompt
# ======================================

if surprise:
    prompt = random.choice(surprise_prompts)
    st.success(f"Random Prompt: **{prompt}**")

# ======================================
# Image Generation
# ======================================

if generate or surprise:

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
        st.stop()

    full_prompt = f"{prompt}, {art_style}"

    # ==============================
    # Assignment Requirement #3
    # Magic Enhance
    # ==============================

    if magic_enhance:
        full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

    encoded_prompt = urllib.parse.quote(full_prompt)

    # ==============================
    # Assignment Requirement #1
    # Width & Height Parameters
    # ==============================

    url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        f"?width={width}&height={height}"
    )

    with st.spinner("Generating Image..."):

        response = requests.get(url)

        if response.status_code == 200:

            image_bytes = response.content

            st.image(
                image_bytes,
                caption="Generated Image",
                use_container_width=True
            )

            # ==============================
            # Assignment Requirement #2
            # Dynamic PNG Download
            # ==============================

            file_name = (
                f"{art_style.lower().replace(' ', '_')}_image.png"
            )

            st.download_button(
                label="⬇️ Download Image",
                data=image_bytes,
                file_name=file_name,
                mime="image/png"
            )

        else:

            st.error("Image generation failed. Please try again.")

# ======================================
# Footer
# ======================================

st.markdown("---")

st.caption("🚀 Built with Streamlit & Pollinations AI")