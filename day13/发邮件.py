import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "2291494711@qq.com"  # 用户名
mail_pass = "easokwbixrxldiai"  # 口令

sender = '2291494711@qq.com'
receivers = ['2431320433@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("蔚超慧", 'utf-8')  # 发件人
message['To'] = Header("贾经理", 'utf-8')   # 收件人

subject = '测试报告——实验示例'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
send_content = 'hi man，你收到附件了吗？'
content_obj = MIMEText(send_content, 'plain', 'utf-8')  # 第一个参数为邮件内容
message.attach(content_obj)

# 构造附件1，发送当前目录下的 t1.txt 文件
att1 = MIMEText(open('计算器.html', 'rb').read(), _subtype='html', _charset='utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件附件中显示什么名字
att1.add_header("Content-Disposition" , 'attachment', filename="计算器.html")
message.attach(att1)

try:
    smtpObj = smtplib.SMTP('smtp.qq.com')
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException:
    print("Error: 无法发送邮件")