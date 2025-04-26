from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "مرحبًا بك في OpenRouter API!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "يرجى إرسال 'prompt'"}), 400
    response = {"result": f"نص مولد بناءً على: {prompt}"}
    return jsonify(response)

if __name__ == "__main__":
    app.run()
