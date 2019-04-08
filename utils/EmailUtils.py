# encoding=utf-8
'''
邮件
'''
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#定义编码格式utf8
charset_utf8 = 'utf-8'


def create_email(myEmail):
    # 生成一个带附件的空的邮件实例
    message = MIMEMultipart()
    # 发件人、收件人、主题
    message['From'] = myEmail.getEmailFrom()
    message['To'] = myEmail.getEmailTo()
    message['Subject'] = Header(myEmail.getEmailSubject(), charset_utf8)
    # 将正文以text的形式插入邮件 注意：此处plain改为text会变成附件
    message.attach(MIMEText(myEmail.getEmailText(), 'plain', 'utf-8'))

    # 读取附件内容
    att1 = MIMEText(open(myEmail.getAnnexPath(), 'rb').read(), 'base64', charset_utf8)
    att1["Content-Type"] = 'application/octet-stream'
    # 生成附件的名称
    att1["Content-Disposition"] = 'attachment; filename=' + myEmail.getAnnexName()
    # 将附件内容插入邮件
    message.attach(att1)
    return message


def send_email(sender, password, receiver, msg):
    try:
        # 方法1：获取邮箱发送服务器
        server = smtplib.SMTP_SSL('smtp.126.com', 465)  # 加密发送，统一端口 465
        # 方法2：发件人邮箱中的SMTP服务器，端口是25
        # server = smtplib.SMTP("smtp.126.com")
        # 方法3：
        # server = smtplib.SMTP()
        # server.connect("smtp.126.com")

        server.ehlo()
        # 登录账号
        server.login(sender, password)
        # 发送邮件。 此处的发件人邮箱账号、收件人邮箱和账号是列表
        server.sendmail(sender, receiver, msg.as_string())
        print('邮件发送成功')
        # 关闭连接
        server.quit()
    except Exception as e:
        # print(traceback.print_exc())
        print("邮件发送失败:", e)
