# -*- coding:utf-8 -*-
import web

# ===========================================================
# URL映射
# ===========================================================
urls = (
    '/index','index',
    '/login','login',
    '/regpage','regpage',
    '/register','register',
    '/findpassword','findpassword',
    '/sendmail','sendmail')

app = web.application(urls, globals())
db = web.database(dbn='mysql',user='root',pw='',db='login_webpy')
# ===========================================================
# 模板文件夹定义
# ===========================================================
render = web.template.render('templates/')
# ===========================================================
# 实现
# ===========================================================
class index:
    def GET(self):
        return render.index()
    def POST(self):
        return self.GET()

class login:
    def POST(self):
        postdata = web.input()
        username = postdata.username
        password = postdata.password
        rslist = getUserByUserName(username)
        if len(rslist)==0:
            return 'user is not exist'
        else:
            if rslist[0].password == password:
                return render.welcome(username)
            else:
                return 'password error'

class regpage:
    def GET(self):
        return render.register_page()

class register:
   def POST(self):
       reg_info = web.input()
       reg_name = reg_info.username
       reg_password = reg_info.password
       reg_password_again = reg_info.password_again
       reg_emailaddress = reg_info.emailaddress
       rslist = getUserByUserName(reg_name)
       if reg_password<>reg_password_again:
           return 'regster FAIL ! the password is not same'
       else:
           if len(rslist)<>0:
               return 'regster FAIL ! the user is exist'
           else:
               ret = AddUserInfo(reg_name,reg_password,reg_emailaddress)
               # return 'regster success'
               raise web.seeother('/index')

class findpassword:
    def GET(self):
        return render.findpassword()

class sendmail:
    def POST(self):
        data = web.input()
        send_username = data.username
        rslist = getUserByUserName(send_username)
        if len(rslist)==0:
            return "the user is not exist"
        else:
            send_address = rslist[0].emailaddress
            send_password = rslist[0].password
            content = 'the password is : %s'%send_password
            ret = send_mail(send_address , 'this is the email for password' , content, '' , '')
            if ret == -1:
                return 'send fail'
            else:
                return 'send sucess , check your email'

# ===========================================================
# 数据库操作
# ===========================================================
# 根据用户名查询用户信息
def getUserByUserName(username):
    list = db.query('select * from login_info where name="'+username+'"')
    name_list=[]
    for i in list:
        name_list.append(i)
    return name_list

# 插入用户信息表
def AddUserInfo(name,password,emailaddress):
    ret = db.query('insert into login_info(name,password,emailaddress) values("'+name+'","'+password+'","'+emailaddress+'")')
    return ret
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

if __name__ == "__main__":
    app.run()