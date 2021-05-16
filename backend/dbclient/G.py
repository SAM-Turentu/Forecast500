# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: G
# CreateTime: 2021/4/29 21:44
# Summary: ''


from backend.dbclient.MongoDB_Client import MongoDBClient
from backend.dbclient.MySQL_Client import MySQLClient
from conf import CONF


class G(object):
    _instance = None

    @classmethod
    def getInstance(cls):
        """
        @func name: 获得实例
        @desc:
        @author: SAM
        @createTime: 2021/4/29 20:35
        @updateTime(upf): 2021/4/29 20:35
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/4/29 20:36
        @updateTime(upf): 2021/4/29 20:36
        """
        self._conf = CONF

    @property
    def mongodb(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/4/29 20:43
        @updateTime(upf): 2021/4/29 20:43
        """
        return MongoDBClient.getInstance(self._conf.mongodb.host, self._conf.mongodb.port)

    @property
    def mysql(self):
        """
        @func name: mysql 数据库连接
        @desc:
        @author: SAM
        @createTime: 2021/5/16 18:38
        @updateTime(upf): 2021/5/16 18:38
        """
        return MySQLClient.getInstance()
