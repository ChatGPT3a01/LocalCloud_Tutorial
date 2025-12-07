# CH2 | 地端與雲端串接概念

從零開始打造 AI 對話應用 - Flask + OpenAI API 完整教學

## 課程簡報

線上觀看簡報：[課程簡報首頁](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/index.html)

### 簡報內容

| Part | 標題 | 說明 |
|------|------|------|
| Part 1 | [環境準備](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/Part1_環境準備.html) | Python、venv 虛擬環境、pip 套件安裝 |
| Part 2 | [Flask 基礎實作](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/Part2_Flask基礎實作.html) | 路由、app.py、Hello World |
| Part 3 | [AI API 串接](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/Part3_AI_API串接.html) | OpenAI API、.env 設定、/chat 端點 |
| Part 4 | [Postman 測試](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/Part4_Postman測試.html) | POST 請求、JSON Body 測試 |
| Part 5 | [Python 腳本測試](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/Part5_Python腳本測試.html) | requests 套件、兩個 CMD 視窗 |
| Part 6 | [網頁介面](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/Part6_網頁介面.html) | HTML、CSS、JavaScript 前端開發 |
| Part 7 | [前後端串接](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/Part7_前後端串接.html) | render_template、fetch API |
| Part 8 | [雲端部署準備](https://chatgpt3a01.github.io/LocalCloud_Tutorial/簡報/Part8_雲端部署準備.html) | Render、Vercel、Railway 介紹 |

## 程式碼下載

本專案提供完整的程式碼範例，讓你可以對照學習。

### 目錄結構

```
LocalCloud_Tutorial/
├── README.md           # 本說明文件
├── 簡報/               # 課程簡報 (HTML)
│   ├── index.html      # 簡報首頁
│   ├── Part1_環境準備.html
│   ├── Part2_Flask基礎實作.html
│   ├── Part3_AI_API串接.html
│   ├── Part4_Postman測試.html
│   ├── Part5_Python腳本測試.html
│   ├── Part6_網頁介面.html
│   ├── Part7_前後端串接.html
│   └── Part8_雲端部署準備.html
├── 截圖/               # 教學截圖
├── 程式碼/             # 範例程式碼
│   ├── 2.3_Flask快速入門/
│   │   └── app.py
│   ├── 2.4_打造AI對話API/
│   │   ├── 階段一_建立AI對話功能/
│   │   │   ├── app.py
│   │   │   ├── test_api.py
│   │   │   └── .env.example
│   │   └── 階段二_優化與錯誤處理/
│   ├── 2.5_美化介面/
│   │   ├── app.py
│   │   ├── templates/
│   │   │   └── index.html
│   │   └── .env.example
│   └── requirements.txt
```

## 快速開始

### 1. 環境準備

```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境 (Windows CMD)
venv\Scripts\activate

# 啟動虛擬環境 (Windows PowerShell)
venv\Scripts\Activate.ps1

# 啟動虛擬環境 (Mac/Linux)
source venv/bin/activate

# 安裝套件
pip install flask openai python-dotenv requests
```

### 2. 設定 API Key

```bash
# 複製範例檔案
copy .env.example .env

# 編輯 .env 檔案，填入你的 OpenAI API Key
OPENAI_API_KEY=sk-proj-你的API金鑰
```

### 3. 執行應用

```bash
python app.py
```

開啟瀏覽器前往 http://localhost:5000

## 技術棧

- **後端**: Python 3.8+, Flask
- **AI**: OpenAI API (GPT-3.5-turbo / GPT-4)
- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **部署**: Render / Vercel / Railway / Netlify

## 安全注意事項

- `.env` 檔案包含 API Key，**絕對不要上傳到 GitHub**
- 確保 `.gitignore` 包含 `.env` 和 `venv/`
- 定期檢查 API 使用量，設定使用上限

## 常見問題

### Q: Flask 啟動時出現 ModuleNotFoundError？

確認已啟動虛擬環境（提示符前有 `(venv)`），並已安裝所需套件：
```bash
pip install flask openai python-dotenv
```

### Q: API 回傳 401 Unauthorized？

檢查 `.env` 檔案中的 API Key 是否正確，確認 Key 仍然有效。

### Q: 測試腳本連不上伺服器？

需要開啟兩個 CMD 視窗：
1. 第一個視窗執行 `python app.py`（保持運行）
2. 第二個視窗執行 `python test_api.py`

## 課程資源

- **Facebook**: [阿亮老師](https://www.facebook.com/iddmail)
- **YouTube**: [阿亮老師頻道](https://www.youtube.com/@Liang-yt02)

---

© 2026 自己架設 AI - 零基礎到大師 | Made with 曾慶良(阿亮老師) ❤️
