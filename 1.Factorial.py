# -*- coding: utf-8 -*-
'''
4、实现一个函数，传入任意一个整数返回其阶乘的值，传入值必须小于10
'''
def Factorial(num):
    if num < 10:
        result = 1
        for i in range(num):
            result = (i+1)*result
        print u"%d的阶乘是%d"%(num,result)
    else:
        print u"输入错误！请输入一个小于10的数字！"

if __name__ == "__main__":
    input_str = raw_input("请输入一个小于10的数字：")
    input_num = int(input_str)
    Factorial(input_num)
