# 🌐 Language Translator Web App

A professional and responsive **Language Translator** web app built using **Flask**, **HTML**, **CSS**, and **deep-translator**.  
It supports **100+ languages**, includes **auto-detection**, and offers a **dark/light theme toggle** for modern usability.

---

## 🚀 Features

- 🌍 Translate between 100+ languages  
- 🧠 Auto-detect source language  
- 🌓 Light/Dark theme toggle  
- 💡 Real-time clean and responsive UI  
- ⚙️ Flask backend with Jinja2 templating  
- 🔤 Uses `deep-translator` and `PyDictionary` for translation and meanings  

---

## 🧩 Project Structure

translator_app/
│
├── app.py # Flask backend logic
├── templates/
│ └── index.html # Frontend HTML template
└── README.md # Documentation


---

## ⚙️ Installation & Setup

### 1. Clone the Repository

``` bash
git clone https://github.com/your-username/translator_app.git
cd translator_app

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

3. Install Required Packages
pip install flask deep-translator PyDictionary

4. Run the Flask App
python app.py

5. Open in Browser
http://127.0.0.1:5000/


🧠 Flask Backend (app.py)

This is the main Python file handling:

Translation logic using GoogleTranslator

Text input and language selection

Passing translated output to the frontend

Example:

from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from PyDictionary import PyDictionary

app = Flask(__name__)
dictionary = PyDictionary()

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
    "Italian": "it",
    "Turkish": "tr",
    "Bengali": "bn",
    "Urdu": "ur",
    "Tamil": "ta",
    "Telugu": "te",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Dutch": "nl",
    "Greek": "el",
    "Hebrew": "he",
    "Thai": "th",
    "Vietnamese": "vi",
    "Swedish": "sv",
    "Polish": "pl",
    "Czech": "cs",
    "Finnish": "fi",
    "Hungarian": "hu",
    "Romanian": "ro",
    "Slovak": "sk",
    "Croatian": "hr",
    "Ukrainian": "uk",
    "Indonesian": "id",
    "Filipino": "tl",
    "Malay": "ms",
    "Afrikaans": "af",
    "Amharic": "am",
    "Persian": "fa",
    "Nepali": "ne",
    "Sinhala": "si",
    "Mongolian": "mn",
    "Swahili": "sw",
    "Zulu": "zu"
}

@app.route("/", methods=["GET", "POST"])
def index():
    text = translated = ""
    selected_source = selected_target = "auto"

    if request.method == "POST":
        text = request.form["text"]
        source = request.form["source_lang"]
        target = request.form["target_lang"]
        try:
            translated = GoogleTranslator(source=source, target=target).translate(text)
            selected_source, selected_target = source, target
        except Exception as e:
            translated = f"Error: {e}"

    return render_template(
        "index.html",
        text=text,
        translated=translated,
        languages=LANGUAGES,
        selected_source=selected_source,
        selected_target=selected_target,
    )

if __name__ == "__main__":
    app.run(debug=True)

🎨 Frontend (templates/index.html)

The frontend is a clean and responsive design with:

Input area for text

Dropdowns for selecting source and target languages

Output section for translation results

Dark/light theme toggle

Preview snippet:

<input type="checkbox" id="themeToggle">
<label for="themeToggle" class="toggle-label">🌗 Toggle Theme</label>

<form method="POST">
    <label class="label">Enter text:</label>
    <textarea name="text" placeholder="Type your text here...">{{ text }}</textarea>

    <label class="label">Source Language:</label>
    <select name="source_lang">
        <option value="auto">Auto Detect</option>
        {% for name, code in languages.items() %}
        <option value="{{ code }}" {% if code==selected_source %}selected{% endif %}>{{ name }}</option>
        {% endfor %}
    </select>

    <label class="label">Target Language:</label>
    <select name="target_lang">
        {% for name, code in languages.items() %}
        <option value="{{ code }}" {% if code==selected_target %}selected{% endif %}>{{ name }}</option>
        {% endfor %}
    </select>

    <button type="submit">Translate</button>
</form>

{% if translated %}
<div class="output">
    <strong>Translation:</strong>
    <p>{{ translated }}</p>
</div>
{% endif %}

🧪 Example Usage
Input	Source	Target	Output
Hello, how are you?	English	French	Bonjour, comment allez-vous ?
आपका नाम क्या है?	Hindi	English	What is your name?
🧰 Dependencies
Library	Use
Flask	Web framework
deep-translator	Translation API
PyDictionary	Word meaning support
Jinja2	HTML templating engine
📜 License

MIT License © 2025
Developed by Chirag — Engineering Student passionate about AI, ML, and full-stack development.

