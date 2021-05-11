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
from backend.core.settings import settings
from conf import CONF
from controllers.HomeController import *

# 项目启动命令添加下面命令，不添加则默认dev环境
# --config-file=conf\\dev.ini
from mapper import db


def runserver():
    tornado.options.parse_command_line()
    app = tornado.web.Application(Route.get_urls(), **settings)
    app.listen(CONF.dd.port)
    # instance 需要调用 current
    mysql_url = f'mysql+sqlalchemy://{CONF.mysql.user}:{CONF.mysql.password}@{CONF.mysql.host}:{CONF.mysql.port}/{CONF.mysql.database}'
    tornado.ioloop.IOLoop.current().run_sync(lambda: db.set_bind(mysql_url))  # 没有成功连接数据库!!!
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    # tornado.ioloop.IOLoop.instance().run_sync(do_insert)
    runserver()
