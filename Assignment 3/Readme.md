# 🧠 Assignment 3 – Memory Vault Chatbot

## 📖 Overview

The **Memory Vault Chatbot** is an upgraded version of the AI Multiverse Chatbot developed as part of the **Virtual Summer Internship 2026 – AI Builder Track**.

This application introduces **state management** using Streamlit's `st.session_state`, allowing the chatbot to remember previous conversations even when the app reruns. Users can interact with multiple AI personalities while maintaining a continuous and engaging chat experience.

---

## ✨ Features

* 🧠 Stateful conversation using `st.session_state`
* 💬 Continuous chat history across interactions
* 🤖 Powered by Google Gemini API
* 🎭 Multiple AI personalities
* 🗂️ Chat history rendered automatically on every rerun
* 🧹 Clear Chat option
* 🔐 Secure API key management using `.env`
* 🎨 Modern Streamlit chat interface

---

## 🎭 Available AI Personalities

* 🤵 Common Indian Man
* 💪 Crazy Salman Khan Fan
* 👦 Little Boy
* 🔥 Motivational Coach
* 💻 Software Engineer
* 👨‍🏫 College Professor
* 😂 Stand-up Comedian
* 🚀 Entrepreneur
* 📚 Friendly Teacher
* 🤖 AI Assistant

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API (`google-genai`)
* python-dotenv

---

## 📂 Project Structure

```text
Assignment-3-Memory-Vault-Chatbot/
│── app.py
│── requirements.txt
│── .env
│── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Mirai-summer-internship-assignments.git
```

### 2. Navigate to the project folder

```bash
cd Assignment-3-Memory-Vault-Chatbot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 🧠 Key Concepts Demonstrated

* Streamlit Session State
* Stateful Chat Applications
* Chat History Management
* Google Gemini API Integration
* Prompt Engineering
* Interactive Streamlit UI
* Environment Variable Management

---

## 📸 Assignment Requirements Covered

* ✅ Initialize `st.session_state`
* ✅ Store chat messages in memory
* ✅ Render previous conversations
* ✅ Use `st.chat_input()`
* ✅ Use `st.chat_message()`
* ✅ Save both user and assistant messages
* ✅ Continuous multi-message conversation

---

## 👨‍💻 Author

**Rishyup Doliya**

Developed as part of the **Virtual Summer Internship 2026 – AI Builder Track**.

---

## 📄 License

This project is intended for educational purposes as part of the Virtual Summer Internship 2026.
