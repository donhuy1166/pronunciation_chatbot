import openai

def generate_feedback(f1, f2, f3):
    prompt = f"""
Tôi đang luyện phát âm tiếng Anh. Dữ liệu từ phân tích âm thanh:
- F1 = {f1} Hz
- F2 = {f2} Hz
- F3 = {f3} Hz

Dựa vào các giá trị formant này, hãy đoán âm tôi đang phát là gì, phân tích lỗi (nếu có), và gợi ý cách sửa bằng tiếng Việt (nếu cần). Hãy thân thiện và dễ hiểu cho người học.
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']
