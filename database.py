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
        '國父紀念館':{
            'title':'國父紀念館',
            'address':'110台北市信義區仁愛路四段505號',
            'latitude':'25.040029',
            'longitude':'121.560241'
        }
    }
    image_data = {
        'joguman':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsmEP1BHmJUhb-36Jn5JY9mcV-AOl9CUeOeQ&s'
    }
    reply = ['text',text] # 預設回覆的文字就是收到的訊息
    if text in message_data:
        reply = ['text',message_data[text.lower()]]
    if text in location_data:
        reply = ['location',location_data[text.lower()]]
    if text in image_data:
        reply = ['image',image_data[text.lower()]]
    return reply