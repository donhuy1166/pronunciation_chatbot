
from flask import Flask, request, render_template, jsonify
import os
import openai
from formant_analysis import extract_formants
from gpt_feedback import generate_feedback

# Khởi tạo Flask app
app = Flask(__name__)
UPLOAD_FOLDER = "audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Đặt API key cho OpenAI (bạn thay bằng key thật của bạn)
openai.api_key = "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"  # Thay bằng OpenAI API key của bạn

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['audio']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Phân tích formant
    f1, f2, f3 = extract_formants(filepath)
    feedback = generate_feedback(f1, f2, f3)

    return jsonify({
        "F1": f1,
        "F2": f2,
        "F3": f3,
        "feedback": feedback
    })

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data['messages']

    # Gửi toàn bộ hội thoại sang GPT
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    reply = res['choices'][0]['message']['content']
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
