import requests

url = "http://127.0.0.1:5000/api/chat"
data = {"message": "你好！我是AI"}
response = requests.post(url, json=data)

print("响应内容：", response.json())
