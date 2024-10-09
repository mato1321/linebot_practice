import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendEmail(txt, source, fileName, email, pwd):
    msg = MIMEMultipart() #創造郵件
    msg.attach(MIMEApplication(source, Name=fileName)) # 變成一個MINE(電子郵件系統識別和傳送)的附件然後附加檔案
    msg['Subject'] = txt   # 標題
    msg['From'] = email    # 寄件者
    msg['To'] = email      # 收件者
    smtp = smtplib.SMTP('smtp.gmail.com', 587) #  Gmail 提供的 SMTP 伺服器的地址, Gmail 所推薦的連接埠
    smtp.ehlo() # 建立 SMTP 連線的第一步
    smtp.starttls() # 確保連線的安全性
    smtp.login(email, pwd) # 登入google帳戶
    status = smtp.send_message(msg) # 發送郵件
    print(status)
    smtp.quit() # 結束與 Gmail 伺服器的連線