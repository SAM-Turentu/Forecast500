# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: run_uat
# CreateTime: 2021/4/22 20:40
# Summary: '测试环境'


import tornado.web
import tornado.ioloop
from backend.core.settings import settings
from conf import CONF


# 项目启动命令添加下面命令，不添加则默认dev环境
# --config-file=conf\\uat.ini


def runserver():
    app = tornado.web.Application([
        (r'/', None),
    ], **settings)
    app.listen(CONF.dd.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    runserver()
