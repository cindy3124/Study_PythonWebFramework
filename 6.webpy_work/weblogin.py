# -*- coding:utf-8 -*-
import web
import sys
from config.url import urls
from views.index import *
#  ===========================================================
#设置python环境为utf-8编码
#  ===========================================================
import sys
print 'default python env coding:', sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print 'current python env coding:', sys.getdefaultencoding()

##session配置
web.config.session_parameters['cookie_name'] = 'webpy_session_id'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 86400, #24 * 60 * 60, # 24 hours   in seconds
web.config.session_parameters['ignore_expiry'] = True
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'

app = web.application(urls, globals())
##session与应用绑定
if web.config.get("_session") is None:
    from web import utils
    store = web.session.DiskStore('sessions')
    user = utils.Storage({
                          "id": "",
                          "name": "",
                          "email": ""
                          })
    session = web.session.Session(app, store,
                                  initializer={
                                      "count": 0,
                                      "status": 0,
                                      "user": user,
                                               })
    web.config._session = session
else:
    session = web.config._session

if __name__ == "__main__":
    app.run()