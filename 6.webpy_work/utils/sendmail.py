# -*- coding:utf-8 -*-
import web
# ===========================================================
# 发送邮件操作
# ===========================================================
def send_mail(send_to, subject, body, cc=None, bcc=None):
    '''''
    @把找回密码的内容作为邮件发送出去
    '''
    try:
        web.config.smtp_server = 'smtp.163.com'   ##邮件发送服务器
        web.config.smtp_port = 25    ##不设置将使用默认端口
        web.config.smtp_username = 'username'   ##邮件服务器的登录名
        web.config.smtp_password = 'password'   ##邮件服务器的登录密码
        web.config.smtp_starttls = True
        send_from = 'webpytest@163.com'    ##发送的邮件
        web.sendmail(send_from, send_to, subject, body, cc=cc, bcc=bcc)
        return 1  #pass
    except Exception, e:
        print e
        return -1 #fail