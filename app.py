# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "<h1>Hello, Flask!</h1>"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    reply = ""
    if request.method == 'POST':
        user_input = request.form.get('message', '')
        # 模拟一个 AI 回复（可接入 GPT）
        reply = f"你说的是：{user_input}"
    return render_template('index.html', reply=reply)

if __name__ == '__main__':
    app.run(debug=True)
