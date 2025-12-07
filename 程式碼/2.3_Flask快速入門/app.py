# 引入 Flask 框架
from flask import Flask

# 建立 Flask 應用程式物件
# __name__ 參數讓 Flask 知道應用程式的位置
app = Flask(__name__)

# 定義路由：當使用者訪問首頁 "/" 時，執行 home 函數
@app.route('/')
def home():
    # 回傳 HTML 內容給使用者
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>我的第一個 Flask 應用</title>
    </head>
    <body>
        <h1>歡迎來到 Flask 世界！</h1>
        <p>這是你的第一個網頁應用。</p>
    </body>
    </html>
    '''

# 定義另一個路由：當使用者訪問 "/hello" 時，執行 hello 函數
@app.route('/hello')
def hello():
    return '<h1>Hello, Flask!</h1><p>這是另一個頁面。</p>'

# 程式進入點：啟動 Flask 應用
# debug=True 讓我們在開發時能看到詳細的錯誤訊息，並自動重載程式
if __name__ == '__main__':
    app.run(debug=True, port=5000)
