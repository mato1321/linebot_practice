import json
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage
from pyexpat.errors import messages
import database
from database import *

app = Flask(__name__)
@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 收到訊息內容並且轉換成文字
    try:
        database.lineBot_account(body)
        if json_data['events'][0]['message']['type'] == 'text':
            message = reply_message(json_data['events'][0]['message']['text']) # 取得訊息文字
            if message[0] == 'text':     # 判斷回傳的是不是文字關鍵字
                linebot_api.reply_message(token, TextSendMessage(text=message[1]))
            if message[0] == 'image':    # 判斷回傳的是不是照片關鍵字
                linebot_api.reply_message(token, ImageSendMessage(original_content_url=message[1],
                                                                  preview_image_url=message[1]))
            if message[0] == 'location': # 判斷回傳的是不是地點關鍵字
                linebot_api.reply_message(token, LocationSendMessage(title=message[1]['title'],
                                                                        address=message[1]['address'],
                                                                        latitude=message[1]['latitude'],
                                                                        longitude=message[1]['longitude']))
        if json_data['events'][0]['message']['type'] == 'sticker':
            package = json_data['events'][0]['message']['packageId']    # 識別貼圖包的ID
            sticker = json_data['events'][0]['message']['stickerId']    # 識別貼圖的ID
            sticker_request = StickerSendMessage(sticker_id=sticker, package_id=package)  # 設定要回傳的表情貼圖
            linebot_api.reply_message(token, sticker_request)           # 回傳訊息
    except:
        print(body)                                          # 如果錯誤，輸出訊息內容
    return 'Success'                                         # Line伺服器會記錄回應，並把他記為成功的標誌。
if __name__ == "__main__":
    app.run()