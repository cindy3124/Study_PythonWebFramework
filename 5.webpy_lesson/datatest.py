# -*- coding:utf-8 -*-
import web

urls = (
    '/index', 'index',
    '/seeother', 'index',
    '/(test1|test2)', 'test',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class index:
    def GET(self):
        par = web.input()
        # 返回页面
        return '<h1>i am index</h1>'

# 跳转定向
class seeother:
    def GET(self):
        raise web.seeother('/index')

class test:
    def GET(self, name):
        return 'i am %s'%name

    def POST(self, name):
        par = web.input()
        return par

    def DEL(self, name):
        pass

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()