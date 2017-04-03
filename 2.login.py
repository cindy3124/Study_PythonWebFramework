# -*- coding: utf-8 -*-
'''
2、使用python编写一个命令程序：里面保存了若干用户成员的信息，用户只有登陆后才能查看这些用户的信息。
即：用户启动python脚本，然后输入用户名密码登陆成功后，使用命令可以查看其他用户信息
'''

user = {'1':'a','2':'b','3':'c'}
user_info = {
    '1':['小丽','女','11111111'],
    '2':['小林','男','11111112'],
    '3':['林艳','女','11111113']
}

# 判断用户名是否存在
def login(username):
    if username in user:
        input_password = raw_input("请输入密码：")
        # 判断密码
        if input_password == user[username]:
            print '登录成功，可查看其他用户信息:'
            print print_info()
        else:
            print '密码错误！'
    else:
        print '不存在用户名为%s的用户'%username

#打印用户信息
def print_info():
    for key in user_info:
        print '%s %s %s'%(user_info[key][0],user_info[key][1],user_info[key][2])

# 输出用户信息
if __name__ == "__main__":
    input_username = raw_input("请输入用户名：")
    login(input_username)







