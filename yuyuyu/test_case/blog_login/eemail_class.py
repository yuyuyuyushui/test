import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
smtpserver = 'smtp.qq.com'
port = 465
sender = '786313105@qq.com'
psw = 'xsbsjbaygmjgbbdg'
receiver = "786313105@qq.com" # 接收人
# ----------2.编辑邮件的内容------
subject = '这个是主题QQ'
body = '<p>这是发送的QQ邮件</p>' # 定义邮件正文为html格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "786313105@qq.com"
msg['subject'] = subject
# ----------3.发送邮件------
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw) # 登录
smtp.sendmail(sender, receiver, msg.as_string()) # 发送
smtp.quit() # 关闭


