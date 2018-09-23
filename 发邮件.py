#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

#smtp服务器
SMTPServer = "smtp.163.com"
#发邮件的地址
sender = "zhx_work_email@163.com"
#发送者的密码
passewd = "123456zhx"

#设置发送的内容
message = "你好啊，朋友，我是周周"
#转换为邮件文本
msg = MIMEText(message)

#标题
msg["Subject"] = "来自帅哥的问候"
#发送者
msg["From"] = sender

#创建（连接）SMTP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)
#登录邮箱
mailServer.login(sender, passewd)
#发送邮件
mailServer.sendmail(sender, ["zhx_work_email@163.com", "809052701@qq.com"], msg.as_string())
#退出邮箱
mailServer.quit()


