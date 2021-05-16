# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseService
# CreateTime: 2021/4/29 21:46
# Summary: ''


from backend.dbclient.G import G
from backend.utils.Decorate import DI


@DI(g=G.getInstance())
class BaseService(object):

    @property
    def mongodb(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/4/29 21:26
        @updateTime(upf): 2021/4/29 21:26
        """
        return self.g.mongodb

    @property
    def mysql(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/16 18:52
        @updateTime(upf): 2021/5/16 18:52
        """
        return self.g.mysql
