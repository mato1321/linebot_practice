import json
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
app = Flask(__name__)
@app.route("/", methods=['POST'])
#重複訊息
def linebot():
    body = request.get_data(as_text=True)                    # 收到訊息內容並且轉換成文字
    try:
        json_data = json.loads(body)                         # 轉化成json格式
        accessToken = '85oGf11DDw16XJph1qDUSkpzo7YkDiqrB02+GXPfXNImeS2W8rtMzV622ML/cos4Hdd6fuladpk2ezX0xb0w68770kvTIzxqUyJ2g1KH9UOCRzFTuApqJJBwJ1CIB+nEHDAfRuoaNoF/0ALA7Jm0EwdB04t89/1O/w1cDnyilFU='
        secret = '751f6b631e24e65986c97bba872efd35'
        linebot_api = LineBotApi(accessToken)                # 串接line去發送訊息或是取得用戶資料
        handler = WebhookHandler(secret)                     # 串接line去接收用戶的動作
        signature = request.headers['X-Line-Signature']      # 得到一個從line伺服器生成的哈希值
        handler.handle(body, signature)                      # 確認是否是來自真的line傳來的訊息
        token = json_data['events'][0]['replyToken']         # 提取第一個事件的token

        if json_data['events'][0]['type'] == 'sticker':
            stickerId = json_data['events'][0]['message']['stickerId']  # 取得 stickerId
            packageId = json_data['events'][0]['message']['packageId']  # 取得 packageId
            sticker_message = StickerSendMessage(sticker_id=stickerId, package_id=packageId)  # 設定要回傳的表情貼圖
            linebot_api.reply_message(token, sticker_message)           # 回傳訊息
        elif json_data['events'][0]['type'] == 'text':
            message = json_data['events'][0]['message']['text']         # 取得訊息文字
            linebot_api.reply_message(token, TextSendMessage(message))  # 回傳訊息

    except:
        print(body)                                          # 如果錯誤，直接輸出內容
    return 'Success'                                         # Line伺服器會記錄回應，並把他記為成功的標誌。

if __name__ == "__main__":
    app.run()