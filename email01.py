import smtplib
# import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header


class EMAIL:
    def __init__(self, info_list):
        self.time = info_list[0]
        self.place = info_list[1]
        self.theme = info_list[2]
        self.department = info_list[3]
        self.url = info_list[4]
        self.e_host = 'smtp.163.com'
        self.e_sender = 'qbhy_2021@163.com'
        self.e_license = 'DKWVJTNLTLPPANAX'
        self.e_receivers = ['3100954150@qq.com']

    def email(self):
        mm = MIMEMultipart()
        mm['From'] = self.e_sender      # 'qbhy_2021<qbhy_2021@163.com>'
        mm['To'] = self.e_receivers[0]  # '此去经年<3100954150@qq.com>,receiver_2_name<**@qq.com>'
        subject_content = '讲座邀请函'
        content = '讲座邀请函\n\n'+f'讲座主题：{self.theme}\n\n'+f'时间：{self.time}\n\n'+f'地点：{self.place}\n\n'+f'详情：{self.url}\n'
        mm['Subject'] = Header(subject_content, 'utf-8')
        message_text = MIMEText(content, 'plain', 'utf-8')
        mm.attach(message_text)
        return mm.as_string()

    def send(self):
        try:
            stp = smtplib.SMTP()
            stp.connect(self.e_host, 25)
            stp.set_debuglevel(1)
            stp.login(self.e_sender, self.e_license)
            stp.sendmail(self.e_sender, self.e_receivers, self.email())
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('error:', e)
        finally:
            stp.quit()


if __name__ == '__main__':
    e = EMAIL(['place', 'time', 'theme', 'url', 'department'])
    e.send()


# mail_host = 'smtp.163.com'
# mail_sender = 'qbhy_2021@163.com'
# mail_license = 'DKWVJTNLTLPPANAX'       # 邮箱SMTP服务授权码
# mail_receivers = ['3100954150@qq.com']
#
# mm = MIMEMultipart()
#
# mm['From'] = mail_sender                   # 'qbhy_2021<qbhy_2021@163.com>'
# mm['To'] = mail_receivers[0]     # '此去经年<3100954150@qq.com>,receiver_2_name<**@qq.com>'
# subject_content = "Python邮件测试"
# mm['Subject'] = Header(subject_content, 'utf-8')
#
#
# body_content = '你好，这是一个测试邮件！'
# message_text = MIMEText(body_content,'plain','utf-8')
# mm.attach(message_text)

# image_data = open(r'E:/表情包/1592738050535.jpg', 'rb')
# message_image = MIMEImage(image_data.read())
# image_name = '表情包.jpg'            # 这两行删去，图片会以.bin结尾，why?
# message_image['Content-Disposition'] = 'attachment;filename = %s'%image_name.encode('utf-8')  ###
# image_data.close()
# mm.attach(message_image)

# atta = MIMEText(open('sample.xlsx', 'rb').read(), 'base64', 'utf-8')
# atta['Content-Disposition'] = 'attachment; filename="sample.xlsx"'
# mm.attach(atta)

# try:
#     stp = smtplib.SMTP()
#     stp.connect(mail_host, 25)
#     stp.set_debuglevel(1)
#     stp.login(mail_sender, mail_license)
#     stp.sendmail(mail_sender, mail_receivers, mm.as_string())
#     stp.quit()
#     print('邮件发送成功')
# except smtplib.SMTPException as e:
#     print('error', e)
