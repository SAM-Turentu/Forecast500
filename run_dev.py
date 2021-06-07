# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: run
# CreateTime: 2021/4/21 22:23
# Summary: '开发环境'


import os
import logging
import colorama
import tornado.log
import tornado.web
import tornado.ioloop
import tornado.options
from backend.core.BaseLog import LogFormatter
from backend.core.Settings import settings
from conf import CONF
from controllers.HomeController import *

# 项目启动命令添加下面命令，不添加则默认dev环境
# --config-file=conf\\dev.ini
# tornado.options.define('log_file_prefix', default=CONF.log.path)
# tornado.options.options.logging = 'error'
tornado.options.log_file_prefix = CONF.log.path
tornado.options.log_rotate_mode = 'time'
tornado.options.log_rotate_when = 'D'
tornado.options.log_rotate_interval = 1
# tornado.options.define('log_rotate_mode', default='time')
# tornado.options.define('log_rotate_when', default='D')
# tornado.options.define('log_rotate_interval', default=1)


def runserver():
    # tornado.options.parse_config_file(path=CONF.log.path)

    tornado.options.parse_command_line()  # 命令行分析模块  与配置文件命令冲突
    colorama.init(autoreset=True)  # windows 控制台颜色输出
    [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    app = tornado.web.Application(Route.get_urls(), **settings)
    app.listen(CONF.dd.port)
    tornado.ioloop.IOLoop.current().start()


# instance 需要调用 current

if __name__ == '__main__':
    # tornado.ioloop.IOLoop.instance().run_sync(do_insert)
    runserver()
