# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from config.settings import *

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

# 根据用户ID查询用户信息
def getUserByUserId(userid):
    list = db.query('select * from login_info where id="'+userid+'"')
    userid_list=[]
    for i in list:
        userid_list.append(i)
    return userid_list

# 插入用户信息表
def AddUserInfo(name,password,emailaddress):
    ret = db.query('insert into login_info(name,password,emailaddress) values("'+name+'","'+password+'","'+emailaddress+'")')
    return ret

# 插入/完善用户个人信息表
def AddUserPersonalInfo(logininfoid,name,sex,birthday ,address ,hobbies ,headimage ,photo ,introduce):
    is_exist = db.query('select * from user_info where logininfoid = "'+logininfoid+'"')
    if len(is_exist)<>0:
        #存在，则修改该记录
        ret = db.query('update user_info set '
                        'name      = "'+name+'"     , '
                        'sex       = "'+sex+'"      , '
                        'birthday  = "'+birthday+'"  , '
                        'address   = "'+address+'"   , '
                        'hobbies   = "'+hobbies+'"   , '
                        'headimage = "'+headimage+'" , '
                        'photo     =  "'+photo+'"    , '
                        'introduce =  "'+introduce+'"  '
                        'where logininfoid = "'+logininfoid+'"')
    else:
        #不存在，则新增该记录
        ret = db.query('insert into user_info( logininfoid , name ,sex ,birthday ,address ,hobbies ,headimage ,photo ,introduce ) '
                   'values("'+logininfoid+'","'+name+'","'+sex+'" ,"'+birthday+'","'+address+'","'+hobbies+'","'+headimage+'","'+photo+'","'+introduce+'" )')
    return ret