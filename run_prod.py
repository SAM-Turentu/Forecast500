# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: run_prod
# CreateTime: 2021/4/22 20:40
# Summary: '生产环境'


import tornado.web
import tornado.ioloop
from backend.core.Settings import settings
from conf import CONF


# 项目启动命令添加下面命令，不添加则默认dev环境
# --config-file=conf\\prod.ini
# python run_prod.py --config-file=conf\\prod.ini


def runserver():
    app = tornado.web.Application([
        (r'/', None),
    ], **settings)
    app.listen(CONF.dd.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    runserver()
