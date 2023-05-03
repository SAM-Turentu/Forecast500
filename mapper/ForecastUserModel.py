# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: ForecastUserDO
# CreateTime: 2021/5/11 20:39
# Summary: ''


import pbkdf2
from mapper.BaseDO import BaseDO
from peewee import *


class ForecastUserModel(BaseDO):
    id = PrimaryKeyField()
    userId = CharField(64, index=True, null=False)
    userPhone = CharField(32, index=True, null=False)
    userPassword = CharField(256)
    userName = CharField(32)
    userBirthday = DateTimeField()
    userEmail = CharField(128)
    userSex = SmallIntegerField(default=0)
    userLoginTime = DateTimeField()
    # createTime = DateTimeField()
    # updateTime = DateTimeField()
    userDelete = SmallIntegerField(default=0)  # 0:正常；1：注销
    userStatus = SmallIntegerField(default=0)  # 1:正常用户
    userDisable = SmallIntegerField(default=0)  # 0:正常；1：禁用  # 需创建扩展表（禁用时长，记录等）
    userVIP = SmallIntegerField(default=0)
    userSource = SmallIntegerField(default=0)

    class Meta:
        table_name = 'forecast_user'

    @property
    def password(self):
        return self.userPassword

    @password.setter
    def password(self, value):
        # self.userPassword = pbkdf2.crypt(value, iterations=0x256)  # pbkdf2 建议不要超过256，数值越大耗时越长
        self.userPassword = value

    def check_password(self, pwd):
        """
        @Author: SAM
        @CreateTime: 2021/7/19 13:32
        @UpdateTime(upf): 2021/7/19 13:32
        @Desc: ''
        """
        if self.userPassword is not None:
            return self.password == pbkdf2.crypt(pwd, self.password, iterations=0x256)
        else:
            return False
