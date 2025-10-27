from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from PyDictionary import PyDictionary

app = Flask(__name__)
dictionary = PyDictionary()

LANGUAGES = LANGUAGES = LANGUAGES = {
    "Afrikaans (South Africa)": "af",
    "Albanian (Albania)": "sq",
    "Amharic (Ethiopia)": "am",
    "Arabic (Middle East & North Africa)": "ar",
    "Armenian (Armenia)": "hy",
    "Assamese (India)": "as",
    "Aymara (Bolivia, Peru)": "ay",
    "Azerbaijani (Azerbaijan)": "az",
    "Bambara (Mali)": "bm",
    "Basque (Spain)": "eu",
    "Belarusian (Belarus)": "be",
    "Bengali (Bangladesh, India)": "bn",
    "Bhojpuri (India)": "bho",
    "Bosnian (Bosnia & Herzegovina)": "bs",
    "Bulgarian (Bulgaria)": "bg",
    "Catalan (Spain)": "ca",
    "Cebuano (Philippines)": "ceb",
    "Chichewa (Malawi)": "ny",
    "Chinese (Simplified) (China)": "zh-CN",
    "Chinese (Traditional) (Taiwan, Hong Kong)": "zh-TW",
    "Corsican (France, Corsica)": "co",
    "Croatian (Croatia)": "hr",
    "Czech (Czech Republic)": "cs",
    "Danish (Denmark)": "da",
    "Dhivehi (Maldives)": "dv",
    "Dogri (India)": "doi",
    "Dutch (Netherlands)": "nl",
    "English (Worldwide)": "en",
    "Esperanto (International)": "eo",
    "Estonian (Estonia)": "et",
    "Ewe (Ghana, Togo)": "ee",
    "Filipino (Philippines)": "tl",
    "Finnish (Finland)": "fi",
    "French (France, Worldwide)": "fr",
    "Frisian (Netherlands, Germany)": "fy",
    "Galician (Spain, Galicia)": "gl",
    "Georgian (Georgia)": "ka",
    "German (Germany)": "de",
    "Greek (Greece)": "el",
    "Guarani (Paraguay)": "gn",
    "Gujarati (India)": "gu",
    "Haitian Creole (Haiti)": "ht",
    "Hausa (Nigeria, Niger)": "ha",
    "Hawaiian (Hawaii, USA)": "haw",
    "Hebrew (Israel)": "iw",
    "Hindi (India)": "hi",
    "Hmong (China, Southeast Asia)": "hmn",
    "Hungarian (Hungary)": "hu",
    "Icelandic (Iceland)": "is",
    "Igbo (Nigeria)": "ig",
    "Ilocano (Philippines)": "ilo",
    "Indonesian (Indonesia)": "id",
    "Irish (Ireland)": "ga",
    "Italian (Italy)": "it",
    "Japanese (Japan)": "ja",
    "Javanese (Indonesia)": "jw",
    "Kannada (India)": "kn",
    "Kazakh (Kazakhstan)": "kk",
    "Khmer (Cambodia)": "km",
    "Kinyarwanda (Rwanda)": "rw",
    "Konkani (India)": "gom",
    "Korean (South Korea, North Korea)": "ko",
    "Krio (Sierra Leone)": "kri",
    "Kurdish (Kurmanji) (Turkey, Iraq, Syria)": "ku",
    "Kurdish (Sorani) (Iraq, Iran)": "ckb",
    "Kyrgyz (Kyrgyzstan)": "ky",
    "Lao (Laos)": "lo",
    "Latin (Historical/Scholarly)": "la",
    "Latvian (Latvia)": "lv",
    "Lingala (DR Congo, Congo)": "ln",
    "Lithuanian (Lithuania)": "lt",
    "Luganda (Uganda)": "lg",
    "Luxembourgish (Luxembourg)": "lb",
    "Macedonian (North Macedonia)": "mk",
    "Maithili (India, Nepal)": "mai",
    "Malagasy (Madagascar)": "mg",
    "Malay (Malaysia, Brunei)": "ms",
    "Malayalam (India)": "ml",
    "Maltese (Malta)": "mt",
    "Maori (New Zealand)": "mi",
    "Marathi (India)": "mr",
    "Meiteilon (Manipuri, India)": "mni-Mtei",
    "Mizo (India)": "lus",
    "Mongolian (Mongolia)": "mn",
    "Myanmar (Myanmar)": "my",
    "Nepali (Nepal)": "ne",
    "Norwegian (Norway)": "no",
    "Odia (India)": "or",
    "Oromo (Ethiopia, Kenya)": "om",
    "Pashto (Afghanistan, Pakistan)": "ps",
    "Persian (Iran)": "fa",
    "Polish (Poland)": "pl",
    "Portuguese (Portugal, Brazil)": "pt",
    "Punjabi (India, Pakistan)": "pa",
    "Quechua (Peru, Bolivia)": "qu",
    "Romanian (Romania)": "ro",
    "Russian (Russia)": "ru",
    "Samoan (Samoa)": "sm",
    "Sanskrit (India)": "sa",
    "Scots Gaelic (Scotland)": "gd",
    "Sepedi (South Africa)": "nso",
    "Serbian (Serbia)": "sr",
    "Sesotho (Lesotho, South Africa)": "st",
    "Shona (Zimbabwe)": "sn",
    "Sindhi (Pakistan, India)": "sd",
    "Sinhala (Sri Lanka)": "si",
    "Slovak (Slovakia)": "sk",
    "Slovenian (Slovenia)": "sl",
    "Somali (Somalia)": "so",
    "Spanish (Spain, Latin America)": "es",
    "Sundanese (Indonesia)": "su",
    "Swahili (East Africa)": "sw",
    "Swedish (Sweden, Finland)": "sv",
    "Tajik (Tajikistan)": "tg",
    "Tamil (India, Sri Lanka)": "ta",
    "Tatar (Russia)": "tt",
    "Telugu (India)": "te",
    "Thai (Thailand)": "th",
    "Tigrinya (Eritrea, Ethiopia)": "ti",
    "Tsonga (South Africa, Mozambique)": "ts",
    "Turkish (Turkey)": "tr",
    "Turkmen (Turkmenistan)": "tk",
    "Twi (Ghana)": "ak",
    "Ukrainian (Ukraine)": "uk",
    "Urdu (Pakistan, India)": "ur",
    "Uyghur (China)": "ug",
    "Uzbek (Uzbekistan)": "uz",
    "Vietnamese (Vietnam)": "vi",
    "Welsh (Wales)": "cy",
    "Xhosa (South Africa)": "xh",
    "Yiddish (Jewish Communities)": "yi",
    "Yoruba (Nigeria, Benin)": "yo",
    "Zulu (South Africa)": "zu"
}

@app.route("/", methods=["GET", "POST"])
def index():
    translated = ""
    meaning = ""
    text = ""
    source_lang = "auto"
    target_lang = "en"

    if request.method == "POST":
        text = request.form["text"]
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]
        try:
            # Translate text
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            
            # Get meaning only if target language is English (PyDictionary supports English)
            if target_lang == "en":
                meaning = dictionary.meaning(text)
            else:
                # Optional: translate meaning to target language (just translate the English meaning)
                english_meaning = dictionary.meaning(text)
                if english_meaning:
                    meaning_text = ""
                    for k, v in english_meaning.items():
                        meaning_text += f"{k}: {', '.join(v)}\n"
                    meaning = GoogleTranslator(source='en', target=target_lang).translate(meaning_text)
                else:
                    meaning = "No meaning found."
        except Exception as e:
            translated = f"Error: {e}"
            meaning = ""

    return render_template(
        "index.html",
        translated=translated,
        meaning=meaning,
        text=text,
        languages=LANGUAGES,
        selected_source=source_lang,
        selected_target=target_lang
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
