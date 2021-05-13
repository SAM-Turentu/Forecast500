# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: __init__.py
# CreateTime: 2021/4/21 22:25
# Summary: ''


import peewee_async

from conf import CONF

db = peewee_async.MySQLDatabase(**CONF.mysql)
