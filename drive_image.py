import io
from googleapiclient.http import MediaIoBaseUpload
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload

UPLOAD_FOLDER = '1V1GKfvrV03Z8wNWybO90gbeu4EWzCGjk'
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:\Coding\DataVisualization_report\drive.json'  # 金鑰檔案
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES) # 建立憑證物件
service = build('drive', 'v3', credentials=creds)

def upload_drive(line_bot_api, json_data):
    msg_id = json_data['events'][0]['message']['id']  # 取得訊息 ID
    message_content = line_bot_api.get_message_content(msg_id)  # 根據訊息 ID 取得訊息內容
    filename = f'{msg_id}.jpg'  # 設定上傳檔案的名稱
    image_bytes = io.BytesIO(message_content.content)  # 將圖片轉換為二進位資料

    # 建立 Google Drive 上傳物件
    media = MediaIoBaseUpload(image_bytes, mimetype='image/jpg', resumable=True)
    file_metadata = {'name': filename, 'parents': [UPLOAD_FOLDER]}

    # 上傳圖片到 Google Drive
    print("正在上傳檔案...")
    file = service.files().create(body=file_metadata, media_body=media).execute()
    file_id = file.get('id')

    # 回傳上傳成功訊息
    reply = f'上傳成功！\n\n查看：https://drive.google.com/drive/folders/{UPLOAD_FOLDER}'
    print(f'雲端檔案ID：{file_id}')
    return reply