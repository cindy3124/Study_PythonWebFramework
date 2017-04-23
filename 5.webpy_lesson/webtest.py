# -*- coding:utf-8 -*- 
import web

#模板文件夹定义
render = web.template.render('templates/',globals={'stat':'aa'})
# 模板全局变量第二种方法
# web.template.Template.global['config']:config

urls = (
    '/index', 'index',
    '/formpage', 'formpage',
    '/formdeal', 'formdeal',
    '/(test1|test2)', 'test',
    '/(.*)', 'default'
)
app = web.application(urls, globals())

class index:
    def GET(self):
        # 带参数模板
        # return render.testWithPar('dataaaa')
        # 不带参数模板
        return render.testWithoutPar()

class formpage:
    def GET(self):
        return render.post()

class formdeal:
    def GET(self):
        par = web.input()
        return par
    def POST(self):
        return self.GET()

class test:
    def GET(self,name):
        pass

class default:
    def GET(self,name):
        pass

if __name__ == "__main__":
    app.run()