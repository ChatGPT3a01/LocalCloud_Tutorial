# 引入必要的套件
from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# 載入環境變數（從 .env 檔案讀取 API Key）
load_dotenv()

# 建立 Flask 應用程式物件
app = Flask(__name__)

# 建立 OpenAI 客戶端
# 從環境變數中安全地取得 API Key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# 首頁路由：顯示歡迎訊息
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>AI 對話應用</title>
    </head>
    <body>
        <h1>AI 對話應用</h1>
        <p>請使用 /chat 端點進行對話</p>
        <p>範例：POST 請求到 http://localhost:5000/chat</p>
    </body>
    </html>
    '''

# AI 對話 API 端點
# methods=['POST'] 表示這個路由只接受 POST 請求
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 步驟1：從請求中取得使用者的訊息
        data = request.json
        user_message = data.get('message', '')

        # 步驟2：驗證訊息不是空的
        if not user_message:
            return jsonify({'error': '訊息不能是空的'}), 400

        # 步驟3：呼叫 OpenAI API 取得 AI 回應
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一個友善的 AI 助手，用繁體中文回答問題。"},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )

        # 步驟4：從 API 回應中提取 AI 的訊息
        ai_message = response.choices[0].message.content

        # 步驟5：將 AI 的回應以 JSON 格式回傳給前端
        return jsonify({
            'success': True,
            'message': ai_message
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# 啟動 Flask 應用
if __name__ == '__main__':
    app.run(debug=True, port=5000)
