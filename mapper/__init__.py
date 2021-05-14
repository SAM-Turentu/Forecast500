# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: __init__.py
# CreateTime: 2021/4/21 22:25
# Summary: ''


import peewee_async

import peewee_async

from conf import CONF

# db = peewee_async.PooledMySQLDatabase(**CONF.mysql)
# db = peewee_async.MySQLDatabase(**CONF.mysql)


database = peewee_async.MySQLDatabase(**CONF.mysql)
objects = peewee_async.Manager(database=database)
database.set_allow_sync(False)
