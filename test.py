from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

UPLOAD_FOLDER = '1V1GKfvrV03Z8wNWybO90gbeu4EWzCGjk'
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:\password\drive.json'  # 金鑰檔案

# 建立憑證
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# 串連服務
service = build('drive', 'v3', credentials=creds)

filename = "mona-s.jpg"            # 要上傳檔案的路徑與名稱
media = MediaFileUpload(filename)  # 建立檔案物件
file = {'name': filename, 'parents': [UPLOAD_FOLDER]}

print("開始上傳檔案...")
file_id = service.files().create(body=file, media_body=media).execute()
print(file_id)   # 印出上傳檔案後的結果