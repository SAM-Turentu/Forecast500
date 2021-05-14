# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseDO
# CreateTime: 2021/5/13 15:50
# Summary: ''


from peewee import *
from mapper import objects


class BaseDO(Model):
    createTime = DateTimeField(verbose_name='创建时间')
    updateTime = DateTimeField(verbose_name='更新时间')

    class Meta:
        database = objects
        # objs = peewee_async.Manager(database)
        # Error, sync query is not allowed! Call the `.set_allow_sync()` or use the `.allow_sync()` context manager.
        # database.set_allow_sync(False)
