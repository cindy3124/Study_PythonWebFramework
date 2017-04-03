# -*- coding: utf-8 -*-
'''
给定{1:'v1',4:'k4',3:'s3',2:'b2'}根据其键值进行排序
'''

#根据键排序
def Sorted_byKey(dic):
    byKey = sorted(dic.items(), key=lambda k: k[0], reverse=False)
    print u"根据【键】排序如下：" + str(byKey)
    return byKey

#根据值排序
def Sorted_byValue(dic):
    byValue = sorted(dic.items(), key=lambda k: k[1], reverse=False)
    print u"根据【值】排序如下：" + str(byValue)
    return byValue

if __name__ == "__main__":
    dic = {1: 'v1', 4: 'k4', 3: 's3', 2: 'b2'}
    ByKey = Sorted_byKey(dic)
    ByValue = Sorted_byValue(dic)
