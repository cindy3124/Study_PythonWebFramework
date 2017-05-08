# -*- coding:utf-8 -*-
import web
import sys
sys.path.append("..")
from config.settings import *
from models.user import *
from utils.sendmail import *

# ===========================================================
# 实现
# ===========================================================
class index:
    def GET(self):
        session = web.config._session
        session.count += 1
        scount = str(session.count)
        return render.index(scount)
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

                #新增session记录名称
                UserId = rslist[0].id
                print UserId,username
                session = web.config._session
                print session.status
                session.status = 0
                print session.status
                cookies = web.cookies()
                print cookies
                web.setcookie('id', UserId)
                web.setcookie('name',username)

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

class PerfectInformation:
    def GET(self):
        id = web.cookies().get('id')
        name = web.cookies().get('name')
        return render.userinfo(name)

class perfectuserinfo:

    def POST(self):
        #send_headimage = web.input(headimage={})
        #send_photo = web.input(photo={})
        data = web.input()
        send_logininfoid = web.cookies().get('id')
        rslist = getUserByUserId(send_logininfoid)
        if len(rslist) == 0:
            return "the user is not exist"
        else:
            send_name = data.name
            send_sex = data.sex
            send_birthday = data.birthday
            send_address = data.address
            send_hobbies = data.hobbies
            send_introduce = data.introduce

            from utils.file_upload import save_file
            send_headimage = save_file()[0]
            send_photo = save_file()[1]

            ret = AddUserPersonalInfo(send_logininfoid, send_name, send_sex, send_birthday, send_address, send_hobbies,
                                      send_headimage, send_photo, send_introduce)
            if ret == -1:
                return 'PERFECT USER INFO fail'
            else:
                return 'PERFECT USER INFO sucess ! '





