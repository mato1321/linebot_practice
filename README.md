# linebot_practice

這是一個使用 Python 與 Flask 實作的 LINE Bot 範例專案，包含回覆文字、圖片、地點訊息，並整合了氣象、地震資訊查詢，以及圖片上傳到 Google Drive 和郵件寄送功能。

---

## 功能特色

- 文字訊息關鍵字回覆（如打招呼、求助等）
- 回傳圖片與地點訊息
- 查詢氣象圖（即時天氣圖片）
- 地震資訊查詢與圖片回傳（使用台灣中央氣象局開放資料）
- 下載用戶傳送的圖片並上傳到 Google Drive
- 將收到的圖片或影片以 Email 寄送到指定信箱
- 回傳使用者傳送的貼圖
- 使用 Flask 作為 Webhook Server，接收 LINE 訊息事件

---

## 環境需求

- Python 3.8+
- Flask 3.0.3
- line-bot-sdk 3.13.0
- protobuf 5.28.2
- google-api-python-client 2.149.0
- 其他依賴套件（requests、google-auth 等）

---

## 安裝方式

1. 建議使用虛擬環境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

2. 安裝所有套件:
pip install -r requirements.txt

## 專案結構

linebot_practice/
│
├── main.py                 # Flask 伺服器與 LINE Bot Webhook 入口
├── Email.py                # 寄送郵件功能模組
├── earthquake.py           # 地震資訊爬取與處理模組
├── drive_image.py          # 圖片上傳至 Google Drive 功能模組
├── database.py             # 資料庫相關功能（未完成或自行擴充）
├── requirements.txt        # Python 套件清單
└── README.md               # 專案說明文件
