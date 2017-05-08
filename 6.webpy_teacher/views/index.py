#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
from config.settings import *

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
        session = web.config._session
        print session.status
        session.status = 0
        print session.status
        cookies = web.cookies()
        print cookies
        web.setcookie('id', '9527')
        return render.testWithoutPar()
        #return render.sub()

class test:
    def GET(self, name):
        try:
            a = 1/0
        except Exception, e:
            print 'e:',e
            print 'message:', e.message
            import traceback
            traceback.print_exc()
            trace = traceback.extract_stack()
            print trace
            info = traceback.format_exc()
            print info
            import sys
            info = sys.exc_info()
            print info
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
        from utils.file_upload import save_file
        save_file()
        return self.GET()

class default:
    def GET(self, name):
        # print web.ctx.env, web.ctx.status
        # web.header('Cache-Control', 'no-cache')
        raise web.seeother('/error?error_msg=error test')
        if not name:
            name = 'Xiaowu'
        return 'Hello, ' + name + '!'

    def POST(self, name):
        #return 'i am in POST'
        #return do_action('***') + 'action line' + do_action('***')
        from utils.sendmail import send_mail
        return send_mail('send_to', 'subject', 'body')
        #return self.GET(name)

class error:
    def GET(self):
        pars = web.input()
        return render.error(pars.get('error_msg'))