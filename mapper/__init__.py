# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: __init__.py
# CreateTime: 2021/4/21 22:25
# Summary: ''


# from gino import Gino
#
# db = Gino()

import peewee_async

from conf import CONF

db = peewee_async.PooledMySQLDatabase(**CONF.mysql)

# db.set_bind('mysql://localhost/forecast500')
