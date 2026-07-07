import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Identity Echo Interface",
    page_icon="📡",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
.main {
    padding-top: 2rem;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📡 The Identity Echo Interface")

st.write(
    "Welcome to the AI Builder Interface.\n\n"
    "Enter your details below and click **Transmit** to send your message."
)

st.divider()

# Input Fields
user_name = st.text_input(
    "👤 Name",
    placeholder="Enter your name"
)

user_message = st.text_area(
    "💬 Message",
    placeholder="Type your message here..."
)

# Button
if st.button("🚀 Transmit"):

    if user_name.strip() == "":
        st.error("Please provide your name.")

    elif user_message.strip() == "":
        st.warning("Please type a message to transmit.")

    else:
        st.success(
            f"Transmission successful! Greetings, **{user_name}**.\n\n"
            f"We received your message:\n\n> {user_message}"
        )

        characters = len(user_message)
        tokens = characters / 4

        st.info(
            f"System Check: Your message contains **{characters}** characters "
            f"and will consume approximately **{tokens:.2f} tokens**."
        )

        st.metric("Estimated Tokens", f"{tokens:.2f}")