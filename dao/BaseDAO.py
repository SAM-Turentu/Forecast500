# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseDAO
# CreateTime: 2021/4/29 21:43
# Summary: ''


from backend.dbclient.G import G
from backend.utils.Decorate import DI


@DI(g=G.getInstance())
class BaseDAO():
    _instance = None

    @classmethod
    def getInstance(cls):
        """
        @func name: 获得实例
        @desc:
        @author: SAM
        @createTime: 2021/4/29 20:25
        @updateTime(upf): 2021/4/29 20:25
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def mongodb(self):
        """
        @func name: 获取 MongoDB client
        @desc:
        @author: SAM
        @createTime: 2021/4/29 20:28
        @updateTime(upf): 2021/4/29 20:28
        """
        return self.g.mongodb

    @property
    def mysql(self):
        """
        @func name: 获取 MySQL client
        @desc:
        @author: SAM
        @createTime: 2021/5/16 18:51
        @updateTime(upf): 2021/5/16 18:51
        """
        return self.g.mysql

