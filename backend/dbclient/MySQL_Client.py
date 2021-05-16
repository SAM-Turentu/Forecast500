# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: MySQL_Client
# CreateTime: 2021/5/16 18:40
# Summary: ''


import peewee_async
from conf import CONF


class MySQLClient(object):
    _instance = None

    @classmethod
    def getInstance(cls):
        """
        @func name: 获取 MySQL 实例对象
        @desc:
        @author: SAM
        @createTime: 2021/5/16 18:42
        @updateTime(upf): 2021/5/16 18:42
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        """
        @func name: mysql 初始化
        @desc:
        @author: SAM
        @createTime: 2021/5/16 18:44
        @updateTime(upf): 2021/5/16 18:44
        """
        self.database = peewee_async.MySQLDatabase(**CONF.mysql)
        self.objects = peewee_async.Manager(self.database)
        self.database.set_allow_sync(False)
