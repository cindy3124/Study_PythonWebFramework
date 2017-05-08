# -*- coding:utf-8 -*-
import web
import os

# ===========================================================
# 数据库配置定义
# ===========================================================
db = web.database(dbn='mysql',user='root',pw='',db='login_webpy')

# ===========================================================
# 模板文件夹定义
# ===========================================================
render = web.template.render('templates/')

##设置模板全局变量
web.template.Template.globals['render'] = render

##设置为debug模式
web.config.debug = True
web.config['work_dir'] = os.getcwd()