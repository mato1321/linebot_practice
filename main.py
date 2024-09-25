import json
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage
from pyexpat.errors import messages

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

        if json_data['events'][0]['message']['type'] == 'text':
            message = json_data['events'][0]['message']['text']         # 取得訊息文字
            if message =='章祖綸':
                img_url = 'https://instagram.ftpe7-1.fna.fbcdn.net/v/t51.29350-15/277795588_1330595974107864_9164530998079126436_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE2NTMuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.ftpe7-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=Bs4NORQG2o0Q7kNvgFTLyhn&edm=ACpohRwBAAAA&ccb=7-5&ig_cache_key=MjgwNTMxNjM3ODk3ODIwNzQ0Ng%3D%3D.3-ccb7-5&oh=00_AYB69C1x0xeZjDHC8FIZYeoun1_gcgmRfUmJ0R48WlPYzg&oe=66F9ACE2&_nc_sid=2d3a3f'
                img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url) #發圖片
                linebot_api.reply_message(token, img_message)                                           #回傳訊息
            elif message == '101':
                location = LocationSendMessage(title='台北 101', address='110台北市信義區信義路五段7號', latitude='25.034095712145003', longitude='121.56489941996108') #建立座標
                linebot_api.reply_message(token, location)                                              #回傳訊息
            linebot_api.reply_message(token, TextSendMessage(message))  # 回傳訊息

        elif json_data['events'][0]['message']['type'] == 'sticker':
            package = json_data['events'][0]['message']['packageId']    # 識別貼圖包的ID
            sticker = json_data['events'][0]['message']['stickerId']    # 識別貼圖的ID
            sticker_request = StickerSendMessage(sticker_id=sticker, package_id=package)  # 設定要回傳的表情貼圖
            linebot_api.reply_message(token, sticker_request)           # 回傳訊息
    except:
        print(body)                                          # 如果錯誤，輸出訊息內容
    return 'Success'                                         # Line伺服器會記錄回應，並把他記為成功的標誌。

if __name__ == "__main__":
    app.run()