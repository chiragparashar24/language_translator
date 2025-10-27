# 🌐 Language Translator 

A Flask-based web application that allows users to **translate text between multiple languages** using the `googletrans` library.  
It includes a **login page** for authentication and a sleek, modern translation interface.

---

## 🚀 Features
- 🔐 User login page before accessing the translator
- 🌍 Translate text between 100+ languages
- 🧠 Auto language detection
- 💨 Fast, accurate translation using Google Translate API
- 🎨 Clean, responsive UI with HTML and CSS

---

## 🧩 Project Structure
translator_app/
│
├── app.py # Main Flask backend file
├── templates/
│ ├── login.html # Login page
│ ├── index.html # Translation interface
│
├── requirements.txt # Dependencies file
└── README.md # Project documentation

---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/chiragparashar24/language_translator.git
cd language_translator

python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

pip install flask googletrans==4.0.0-rc1
pip freeze > requirements.txt

python app.py
