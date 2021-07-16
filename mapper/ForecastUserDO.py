# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: ForecastUserDO
# CreateTime: 2021/5/11 20:39
# Summary: ''


from mapper.BaseDO import BaseDO
from peewee import *


class ForecastUserDO(BaseDO):
    id = PrimaryKeyField()
    userId = CharField(64, index=True, null=False)
    userPhone = CharField(32, index=True, null=False)
    userPassword = CharField(32)
    userName = CharField(32)
    userBirthday = DateTimeField()
    userEmail = CharField(128)
    userSex = SmallIntegerField(default=0)
    userLoginTime = DateTimeField()
    # createTime = DateTimeField()
    # updateTime = DateTimeField()
    userDelete = SmallIntegerField(default=0)
    userStatus = SmallIntegerField(default=0)
    userDisable = SmallIntegerField(default=0)
    userVIP = SmallIntegerField(default=0)
    userSource = SmallIntegerField(default=0)

    class Meta:
        table_name = 'forecast_user'

    # @property
    # def userId(self):
    #     return self.userId
    #
    # @userId.setter
    # def userId(self, value):
    #     self.userId = value
