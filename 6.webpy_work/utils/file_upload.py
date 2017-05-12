# -*- coding:utf-8 -*-
import web
import os
from datetime import *

def save_file():
    x = web.input(headimage={})
    y = web.input(photo={})
    ##测试代码
    #web.debug(send_headimage['headimage'].filename) # This is the filename
    #web.debug(send_headimage['headimage'].value) # This is the file contents
    #web.debug(send_headimage['headimage'].file.read()) # Or use a file(-like) object

    # change this to the directory you want to store the file in.
    filedir = os.path.join( web.config['work_dir'], 'static', 'upload_files' )

    filename_list = []

    if 'headimage' in x:  # to check if the file-object is created
        filepath = x.headimage.filename.replace('\\', '/')  # replaces the windows-style slashes with linux ones.
        filename = filepath.split('/')[-1]  # splits the and chooses the last part (the filename with extension)
        ext = filename.split('.',1)[1]  # 获取后缀名
        now = datetime.now()
        t = 'headimage_%d%d%d%d%d%d'%(now.year, now.month, now.day ,now.hour ,now.minute ,now.second)
        filename =t+'.'+ext
        filename = filename.decode('utf-8')  ##decoding for windows file name
        print filename
        fout = open(filedir + '/' + filename, 'wb')  # creates the file where the uploaded file should be stored
        fout.write(x.headimage.file.read())  # writes the uploaded file to the newly created file.
        fout.close()  # closes the file, upload complete.
        filename_list.append(filename)

    if 'photo' in y:  # to check if the file-object is created
        filepath = y.photo.filename.replace('\\', '/')  # replaces the windows-style slashes with linux ones.
        filename = filepath.split('/')[-1]  # splits the and chooses the last part (the filename with extension)
        ext = filename.split('.',1)[1]  # 获取后缀名
        now = datetime.now()
        t = 'photo_%d%d%d%d%d%d'%(now.year, now.month, now.day ,now.hour ,now.minute ,now.second)
        filename =t+'.'+ext
        filename = filename.decode('utf-8')  ##decoding for windows file name
        print filename
        fout = open(filedir + '/' + filename, 'wb')  # creates the file where the uploaded file should be stored
        fout.write(y.photo.file.read())  # writes the uploaded file to the newly created file.
        fout.close()  # closes the file, upload complete.
        filename_list.append(filename)

    return filename_list
        # raise web.seeother('/perfectuserinfo')

