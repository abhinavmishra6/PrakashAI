from flask import Flask, render_template, request, jsonify

from backend.stt import listen
from backend.translator import to_english,to_hindi
from backend.brain import get_response
from backend.tts import speak
import warnings
import asyncio

warnings.filterwarnings("ignore", category=ResourceWarning)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/voice", methods=["POST"])
def voice_input():
    text = listen()

    if not text:
        return jsonify({"response": "I could not hear you"})
    return jsonify({"user": text})

@app.route("/text", methods=["POST"])
def text_input():
    user_text = request.json["text"]
    response = get_response(user_text)
    hinResponse = to_hindi(response)
    result = jsonify({"response": response})
    speak(hinResponse, "hi")
    return result


if __name__ == "__main__":
    app.run(debug=False)
