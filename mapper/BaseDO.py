# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseDO
# CreateTime: 2021/5/13 15:50
# Summary: ''


from peewee import *

from backend.dbclient.MySQL_Client import MySQLClient


class Base(Model):

    @property
    def dict(self):
        """
        @func name:
        @desc: 
        @author: SAM
        @createTime: 2021/5/16 19:20
        @updateTime(upf): 2021/5/16 19:20
        """
        return self

    def to_json(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/16 19:21
        @updateTime(upf): 2021/5/16 19:21
        """
        return {'data': self}


class BaseDO(Model):
    createTime = DateTimeField(verbose_name='创建时间')
    updateTime = DateTimeField(verbose_name='更新时间')

    class Meta:
        database = MySQLClient.getInstance().database
