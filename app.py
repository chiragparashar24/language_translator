from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from PyDictionary import PyDictionary

app = Flask(__name__)
dictionary = PyDictionary()

LANGUAGES = {
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
    "Bhojpuri (India, Nepal)": "bho",
    "Bosnian (Bosnia & Herzegovina)": "bs",
    "Bulgarian (Bulgaria)": "bg",
    "Catalan (Spain)": "ca",
    "Cebuano (Philippines)": "ceb",
    "Chinese (Simplified, China)": "zh-CN",
    "Chinese (Traditional, Taiwan)": "zh-TW",
    "Corsican (France - Corsica)": "co",
    "Croatian (Croatia)": "hr",
    "Czech (Czech Republic)": "cs",
    "Danish (Denmark)": "da",
    "Dhivehi (Maldives)": "dv",
    "Dogri (India)": "doi",
    "Dutch (Netherlands, Belgium)": "nl",
    "English (Worldwide)": "en",
    "Esperanto (International)": "eo",
    "Estonian (Estonia)": "et",
    "Ewe (Ghana, Togo)": "ee",
    "Filipino (Philippines)": "tl",
    "Finnish (Finland)": "fi",
    "French (France, Africa, Canada)": "fr",
    "Frisian (Netherlands)": "fy",
    "Galician (Spain)": "gl",
    "Georgian (Georgia)": "ka",
    "German (Germany, Austria, Switzerland)": "de",
    "Greek (Greece, Cyprus)": "el",
    "Guarani (Paraguay)": "gn",
    "Gujarati (India)": "gu",
    "Haitian Creole (Haiti)": "ht",
    "Hausa (Nigeria, Niger)": "ha",
    "Hawaiian (Hawaii, USA)": "haw",
    "Hebrew (Israel)": "he",
    "Hindi (India)": "hi",
    "Hmong (China, Vietnam, Laos)": "hmn",
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
    "Kurdish (Kurmanji, Turkey)": "ku",
    "Kurdish (Sorani, Iraq)": "ckb",
    "Kyrgyz (Kyrgyzstan)": "ky",
    "Lao (Laos)": "lo",
    "Latin (Ancient Europe)": "la",
    "Latvian (Latvia)": "lv",
    "Lingala (Congo, DRC)": "ln",
    "Lithuanian (Lithuania)": "lt",
    "Luxembourgish (Luxembourg)": "lb",
    "Macedonian (North Macedonia)": "mk",
    "Maithili (India, Nepal)": "mai",
    "Malagasy (Madagascar)": "mg",
    "Malay (Malaysia, Brunei, Singapore)": "ms",
    "Malayalam (India)": "ml",
    "Maltese (Malta)": "mt",
    "Maori (New Zealand)": "mi",
    "Marathi (India)": "mr",
    "Meiteilon (Manipuri, India)": "mni-Mtei",
    "Mizo (India)": "lus",
    "Mongolian (Mongolia)": "mn",
    "Myanmar (Burmese, Myanmar)": "my",
    "Nepali (Nepal, India)": "ne",
    "Norwegian (Norway)": "no",
    "Nyanja (Malawi, Zambia)": "ny",
    "Odia (India)": "or",
    "Oromo (Ethiopia, Kenya)": "om",
    "Pashto (Afghanistan, Pakistan)": "ps",
    "Persian (Iran, Afghanistan, Tajikistan)": "fa",
    "Polish (Poland)": "pl",
    "Portuguese (Portugal, Brazil)": "pt",
    "Punjabi (India, Pakistan)": "pa",
    "Quechua (Peru, Bolivia, Ecuador)": "qu",
    "Romanian (Romania, Moldova)": "ro",
    "Russian (Russia, Belarus)": "ru",
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
    "Somali (Somalia, Kenya)": "so",
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
    "Turkish (Turkey, Cyprus)": "tr",
    "Turkmen (Turkmenistan)": "tk",
    "Twi (Akan, Ghana)": "ak",
    "Ukrainian (Ukraine)": "uk",
    "Urdu (Pakistan, India)": "ur",
    "Uyghur (China)": "ug",
    "Uzbek (Uzbekistan)": "uz",
    "Vietnamese (Vietnam)": "vi",
    "Welsh (Wales)": "cy",
    "Xhosa (South Africa)": "xh",
    "Yiddish (Israel, Europe)": "yi",
    "Yoruba (Nigeria, Benin)": "yo",
    "Zulu (South Africa)": "zu"
}

  
@app.route("/", methods=["GET", "POST"])
def translator():
    translated = ""
    meaning = ""
    text = ""
    source_lang = "auto"
    target_lang = "en"

    if request.method == "POST":
        text = request.form["text"].strip()
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]

        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            if target_lang == "en":
                word_meaning = dictionary.meaning(text)
                if word_meaning:
                    meaning = "\n".join([f"{k}: {', '.join(v)}" for k, v in word_meaning.items()])
                else:
                    meaning = "No meaning found."
            else:
                meaning = "Meaning available only for English translations."
        except Exception as e:
            translated = f"Error: {e}"

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
