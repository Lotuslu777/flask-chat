# import requests
# from flask import Flask, request, render_template

# app = Flask(__name__)

# DEEPSEEK_API_KEY = "sk-a03b76f568564290a9492a99f6673fd5"

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     reply = ""
#     if request.method == 'POST':
#         user_input = request.form.get('message', '')

#         # 调用 DeepSeek Chat API
#         url = "https://api.deepseek.com/v1/chat/completions"
#         headers = {
#             "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
#             "Content-Type": "application/json"
#         }
#         payload = {
#             "model": "deepseek-chat",
#             "messages": [
#                 {"role": "user", "content": user_input}
#             ]
#         }
#         res = requests.post(url, headers=headers, json=payload)
#         try:
#             reply = res.json()['choices'][0]['message']['content']
#         except:
#             reply = "AI 回复失败，请检查 API 响应"

#     return render_template('index.html', reply=reply)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="sk-a03b76f568564290a9492a99f6673fd5", base_url="https://api.deepseek.com/v1")

@app.route('/', methods=['GET', 'POST'])
def index():
    reply = ""
    if request.method == 'POST':
        user_input = request.form.get('message', '')

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": user_input}
            ],
            stream=False
        )
        reply = response.choices[0].message.content

    return render_template('index.html', reply=reply)

if __name__ == '__main__':
    app.run(debug=True)
