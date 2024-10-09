import json
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
#from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage
#from pyexpat.errors import messages
import Email
#import database
from database import *
#from  Email import *
#import drive_image
from drive_image import *

app = Flask(__name__)
@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 收到訊息內容並且轉換成文字
    try:
        json_data = json.loads(body)  # 轉化成json格式
        accessToken = '85oGf11DDw16XJph1qDUSkpzo7YkDiqrB02+GXPfXNImeS2W8rtMzV622ML/cos4Hdd6fuladpk2ezX0xb0w68770kvTIzxqUyJ2g1KH9UOCRzFTuApqJJBwJ1CIB+nEHDAfRuoaNoF/0ALA7Jm0EwdB04t89/1O/w1cDnyilFU='
        secret = '751f6b631e24e65986c97bba872efd35'
        linebot_api = LineBotApi(accessToken)  # 串接line去發送訊息或是取得用戶資料
        handler = WebhookHandler(secret)  # 串接line去接收用戶的動作
        signature = request.headers['X-Line-Signature']  # 得到一個從line伺服器生成的哈希值
        handler.handle(body, signature)  # 確認是否是來自真的line傳來的訊息
        token = json_data['events'][0]['replyToken']  # 提取第一個事件的token
        msgID = json_data['events'][0]['message']['id'] #提取訊息的ID編號

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

        if json_data['events'][0]['message']['type'] == 'image':
            linebot_api.reply_message(token, TextSendMessage(upload_drive(linebot_api, json_data, msgID)))  # 上傳雲端並且回傳訊息
            message_content = linebot_api.get_message_content(msgID) # 下載圖片
            Email.sendEmail('傳送line收到的圖片', message_content.content, f'{msgID}.jpg', 'charleskao811@gmail.com', 'sdce hath widj kyqe')

        if json_data['events'][0]['message']['type'] == 'video':
            message_content = linebot_api.get_message_content(msgID) # 下載影片
            Email.sendEmail('傳送line收到的影片', message_content.content, f'{msgID}.mp4', 'charleskao811@gmail.com', 'sdce hath widj kyqe')

    except:
        print(body)                                          # 如果錯誤，輸出訊息內容
    return 'Success'                                         # Line伺服器會記錄回應，並把他記為成功的標誌。

if __name__ == "__main__":
    app.run()