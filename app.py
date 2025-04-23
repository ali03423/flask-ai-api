from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        result = response.json()
        return jsonify({"result": result["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
