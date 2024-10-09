import json
from flask import request
from linebot import LineBotApi, WebhookHandler
def lineBot_account(body):
    json_data = json.loads(body)  # 轉化成json格式
    accessToken = '85oGf11DDw16XJph1qDUSkpzo7YkDiqrB02+GXPfXNImeS2W8rtMzV622ML/cos4Hdd6fuladpk2ezX0xb0w68770kvTIzxqUyJ2g1KH9UOCRzFTuApqJJBwJ1CIB+nEHDAfRuoaNoF/0ALA7Jm0EwdB04t89/1O/w1cDnyilFU='
    secret = '751f6b631e24e65986c97bba872efd35'
    linebot_api = LineBotApi(accessToken)  # 串接line去發送訊息或是取得用戶資料
    handler = WebhookHandler(secret)  # 串接line去接收用戶的動作
    signature = request.headers['X-Line-Signature']  # 得到一個從line伺服器生成的哈希值
    handler.handle(body, signature)  # 確認是否是來自真的line傳來的訊息
    token = json_data['events'][0]['replyToken']  # 提取第一個事件的token
    return token, json_data


# 定義回覆訊息的函式
def reply_message(text):
    # 創造字典來去客製化回覆訊息
    message_data = {
        'hi':'Hi! 你好呀～',
        'hello':'Hello World!!!!',
        '你好':'你好呦～',
        'help':'有什麼要幫忙的嗎？'
    }
    location_data = {
        '洪幹家':{
            'title':'洪幹家',
            'address':'100台北市松山區延吉街27-1號',
            'latitude':'25.045977749227838',
            'longitude':'121.55373368255879'
        }
    }
    image_data = {
        '章祖綸':'https://scontent-tpe1-1.cdninstagram.com/v/t51.29350-15/277795588_1330595974107864_9164530998079126436_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE2NTMuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=scontent-tpe1-1.cdninstagram.com&_nc_cat=100&_nc_ohc=Bs4NORQG2o0Q7kNvgHlqGUT&_nc_gid=e59c2bcccff04b24848d457804b9f042&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MjgwNTMxNjM3ODk3ODIwNzQ0Ng%3D%3D.3-ccb7-5&oh=00_AYCU20YID74XOEG0iYyNWzt7ePSs5ib1Nrrqqxhr_3KF1A&oe=66F9E522&_nc_sid=7a9f4b'
    }
    reply = ['text',text] # 預設回覆的文字就是收到的訊息
    if text in message_data:
        reply = ['text',message_data[text.lower()]]
    if text in location_data:
        reply = ['location',location_data[text.lower()]]
    if text in image_data:
        reply = ['image',image_data[text.lower()]]
    return reply