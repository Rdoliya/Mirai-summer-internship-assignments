# 🎮 Assignment 5 – Multi-Modal Visual Novel

## 📖 Overview

The **Multi-Modal Visual Novel** is the capstone project developed during the **Virtual Summer Internship 2026 – AI Builder Track**.

This application combines **AI-powered storytelling**, **image generation**, and **text-to-speech narration** into an interactive "Choose Your Own Adventure" experience. Users influence the story by selecting dynamically generated choices, with each decision producing a new chapter, a matching AI-generated illustration, and narrated audio.

---

## ✨ Features

* 📚 AI-powered interactive storytelling
* 🤖 Google Gemini API integration
* 🖼️ AI-generated illustrations using Pollinations AI
* 🔊 Text-to-Speech narration with gTTS
* 🎮 Dynamic choice buttons generated from AI responses
* 📦 JSON-based structured communication
* 🧠 Stateful gameplay using Streamlit Session State
* ⚙️ Story Genre and Art Style customization
* 🛡️ Graceful error handling with `try...except`
* 🔄 Restart Story option

---

## 🎭 Story Genres

* Fantasy
* Science Fiction
* Mystery
* Horror
* Adventure
* Romance
* Cyberpunk
* Historical Fiction

---

## 🎨 Art Styles

* Realistic
* Anime
* Fantasy Art
* Pixel Art
* Oil Painting
* Watercolor
* Cyberpunk
* Sketch
* Digital Art
* 3D Render

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API (`google-genai`)
* Pollinations AI
* gTTS (Google Text-to-Speech)
* Requests
* Pillow
* python-dotenv
* JSON

---

## 📂 Project Structure

```text
Assignment-5-Multi-Modal-Visual-Novel/
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
git clone https://github.com/Rdoliya/Mirai-summer-internship-assignments.git
```

### 2. Navigate to the project folder

```bash
cd Assignment-5-Multi-Modal-Visual-Novel
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

* AI Prompt Engineering
* Structured JSON Parsing
* Dynamic UI Generation
* Stateful Streamlit Applications
* Text-to-Speech Integration
* Image Generation APIs
* Error Handling with `try...except`
* Session State Management

---

## 📸 Assignment Requirements Covered

* ✅ Cached Gemini Client
* ✅ Story Settings Sidebar
* ✅ JSON Parsing
* ✅ Dynamic Choice Buttons
* ✅ Pollinations AI Image Rendering
* ✅ Text-to-Speech Narration
* ✅ Stateful Story Memory
* ✅ Error Handling with Toast Notifications

---

## 👨‍💻 Author

**Rishyup Doliya**

Developed as part of the **Virtual Summer Internship 2026 

---

## 📄 License

This project is intended for educational purposes as part of the Virtual Summer Internship 2026.
