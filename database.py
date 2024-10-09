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
        '章祖綸':'https://instagram.ftpe8-2.fna.fbcdn.net/v/t51.29350-15/277795588_1330595974107864_9164530998079126436_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE2NTMuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.ftpe8-2.fna.fbcdn.net&_nc_cat=100&_nc_ohc=0LStoLer2poQ7kNvgFc_CHC&_nc_gid=425ce348c7d94defb535b0685476e4f0&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MjgwNTMxNjM3ODk3ODIwNzQ0Ng%3D%3D.3-ccb7-5&oh=00_AYAAjmbC5GagIEsUeupK8gpZXi02cWYW9RRSSrwe65Ch0A&oe=670BE9A2&_nc_sid=7a9f4b'
    }
    reply = ['text',text] # 預設回覆的文字就是收到的訊息
    if text in message_data:
        reply = ['text',message_data[text.lower()]]
    if text in location_data:
        reply = ['location',location_data[text.lower()]]
    if text in image_data:
        reply = ['image',image_data[text.lower()]]
    return reply