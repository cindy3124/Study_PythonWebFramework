#!/usr/bin/python
# -*- coding: utf-8 -*-
import web

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
        send_from = 'username@163.com'    ##发送的邮件
        web.sendmail(send_from, send_to, subject, body, cc=cc, bcc=bcc)
        return 1  #pass
    except Exception, e:
        print e
        return -1 #fail

if __name__=='__main__':
    send_to = ['someone1@qq.com', 'someone2@sina.com']
    subject = '邮件标题'
    body = '邮件内容\n可以有回车'
    cc = ['someone1@qq.com', 'someone2@sina.com']   ##抄送
    bcc = ['someone1@qq.com', 'someone2@sina.com']  ##密抄
    send_mail(send_to, subject, body, cc, bcc)
