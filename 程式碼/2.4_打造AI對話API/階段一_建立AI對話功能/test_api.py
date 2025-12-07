# 引入 requests 套件
import requests

# 定義 API 端點網址
url = 'http://localhost:5000/chat'

# 準備要發送的訊息
data = {
    'message': '你好，請介紹一下你自己'
}

# 發送 POST 請求
response = requests.post(url, json=data)

# 印出回應
print('狀態碼:', response.status_code)
print('回應內容:', response.json())
