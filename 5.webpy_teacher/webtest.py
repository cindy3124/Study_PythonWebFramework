#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
from action import do_action

##模板文件夹定义
render = web.template.render('templates/')
#render = web.template.render('templates/', base='base')
web.template.Template.globals['render'] = render
db = web.database(dbn='mysql', host='localhost', port=3306, user='root', pw='changeit!', db='test')

urls = (
    '/database', 'database',
    '/index', 'index',
    '/formpage', 'formpage',
    '/formdeal', 'formdeal',
    '/(test1|test2)', 'test',
    '/(.*)', 'default'
)

app = web.application(urls, globals())

class database:
    def GET(self):
        rt = db.select('20w', limit='0,10')
        for r in rt:
            print r
        return '200'

class index:
    def GET(self):
        #return 'i am index page'
        #return render.testWithPar('dataguru')
        return render.testWithoutPar()
        #return render.sub()

class test:
    def GET(self, name):
        return 'i am %s page' % name

class formpage:
    def GET(self):
        return render.post()

class formdeal:
    def GET(self):
        pars = web.input()
        print pars
        return pars

    def POST(self):
        return self.GET()

class default:
    def GET(self, name):
        if not name:
            name = 'Xiaowu'
        return 'Hello, ' + name + '!'

    def POST(self, name):
        #return 'i am in POST'
        #return do_action('***') + 'action line' + do_action('***')
        from sendmail import send_mail
        return send_mail('send_to', 'subject', 'body')
        #return self.GET(name)

if __name__ == "__main__":
    app.run()