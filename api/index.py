from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# رابط API الخاص بـ OpenRouter
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# مفتاح API الخاص بك
API_KEY = "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"

@app.route("/", methods=["GET"])
def home():
    return "مرحباً بك في API الذكاء الاصطناعي باستخدام OpenRouter!"

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(OPENROUTER_API_URL, headers=headers, json=body)
        response_data = response.json()

        if response.status_code != 200:
            return jsonify({"error": response_data}), response.status_code

        result = response_data['choices'][0]['message']['content']
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
