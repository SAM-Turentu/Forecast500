# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: ForecastUserDO
# CreateTime: 2021/5/11 20:39
# Summary: ''


# from mapper import db
# from gino import Gino
# from sqlalchemy import *

# db = Gino()
from backend.utils.Result import ReturnJson
from mapper.BaseDO import BaseDO
from peewee import *


# class ForecastUserDO(db.Model):
#     __tablename__ = 'forecast_user'
#     id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#     userId = db.Column(db.CHAR(32), index=True, nullable=False)
#     userPhone = db.Column(db.CHAR(32), index=True, nullable=False)
#     userPassword = db.Column(db.CHAR(32))
#     userName = db.Column(db.VARCHAR(64))
#     userBirthday = db.Column(db.DateTime())
#     userEmail = db.Column(db.VARCHAR(128))
#     userSex = db.Column(db.SMALLINT(), default=0)
#     userLoginTime = db.Column(db.DateTime())
#     userCreateTime = db.Column(db.DateTime())
#     userUpdateTime = db.Column(db.DateTime())
#     userDelete = db.Column(db.SMALLINT(), default=0)
#     userStatus = db.Column(db.SMALLINT(), default=0)
#     userDisable = db.Column(db.SMALLINT(), default=0)
#     userVIP = db.Column(db.SMALLINT(), default=0)


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

    class Meta:
        table_name = 'forecast_user'


class UserService:

    async def add_user(self, userId, userPhone, userName):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/11 22:15
        @updateTime(upf): 2021/5/11 22:15
        """

        await ForecastUserDO.create(userId=userId, userPhone=userPhone, userName=userName)
        return ReturnJson.success(data={'userName': 'SAM', 'userPhone': '18292007162'})
