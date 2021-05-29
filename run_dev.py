# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: run
# CreateTime: 2021/4/21 22:23
# Summary: '开发环境'


import tornado.web
import tornado.ioloop
import tornado.options
from backend.core.Settings import settings
from conf import CONF
from controllers.HomeController import *


# 项目启动命令添加下面命令，不添加则默认dev环境
# --config-file=conf\\dev.ini


def runserver():
    # tornado.options.parse_command_line()
    app = tornado.web.Application(Route.get_urls(), **settings)
    app.listen(CONF.dd.port)
    tornado.ioloop.IOLoop.current().start()


# instance 需要调用 current

if __name__ == '__main__':
    # tornado.ioloop.IOLoop.instance().run_sync(do_insert)
    runserver()
