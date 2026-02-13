# Prakash AI Assistant

>  A full-stack AI assistant built with Flask, Ollama, Selenium, and Edge TTS.
>  Created by **Abhinav Mishra**.

------

## Overview

Prakash AI is a locally running, privacy-focused AI assistant that supports:

- Voice Input (Speech Recognition)
- Text-to-Speech (Hindi & English)
- Local LLM via Ollama
- Browser Automation (Google, YouTube, WhatsApp)
- System Automation (VS Code, Shutdown, Time)
- Modern Chat UI (Dark / Light Mode)

All processing runs locally on your machine.

------

## Tech Stack

- Backend: Flask
- LLM Runtime: Ollama
- Model: Custom phi4-mini (Prakash personality)
- Automation: Selenium
- Speech Recognition: Google STT
- Text-to-Speech: Edge TTS
- Frontend: HTML, CSS, JavaScript

------

## Project Structure

```
prakash-ai/
│
├── app.py
├── Modelfile
├── requirements.txt
│
├── backend/
│   ├── brain.py
│   ├── automation.py
│   ├── browserControl.py
│   ├── stt.py
│   ├── tts.py
│   └── translator.py
│
├── static/
│   ├── script.js
│   └── style.css
│
└── templates/
    └── index.html
```

------

## Features

### 🔹 AI Chat

- Natural conversation
- Hindi + English understanding
- Custom personality model

### 🔹 Voice Interaction

- Speak to the assistant
- Assistant replies in Hindi

### 🔹 Google Automation

- Search Google
- Open first result
- Scroll up/down
- Open specific website

### 🔹 YouTube Automation

- Search videos
- Play specific video

### 🔹 WhatsApp Automation

- Open WhatsApp Web
- Send message to contact

### 🔹 System Controls

- Open VS Code
- Get current time
- Shutdown PC

------

## Setup Instructions

### 1️⃣ Install Python 3.10+

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

------

### 3️⃣ Install Ollama

Download from:
 https://ollama.com

Pull model:

```
ollama pull phi4-mini
```

Create custom model:

```
ollama create prakashFast -f Modelfile
```

Start Ollama:

```
ollama serve
```

------

### 4️⃣ Run Application

```
python app.py
```

Open:

```
http://127.0.0.1:5000
```

------

## Privacy

- Fully local AI
- No cloud API calls
- No OpenAI key required
- Runs offline (except Google STT & Edge TTS)

------

## Demo Commands

Try:

```
search in google for machine learning roadmap
open website github
scroll down
open youtube
play video python tutorial
open whatsapp
send whatsapp message to Rahul saying hello
```

------

## Future Improvements

- Long-term memory storage
- Emotion detection
- LLM-based intent detection
- Tab management
- Smart result selection
- Encrypted memory

------

## Author

**Abhinav Mishra**
 B.Tech CSE | VIT Chennai
 Built with ❤️ and Python