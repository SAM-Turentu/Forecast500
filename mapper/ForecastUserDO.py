# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: ForecastUserDO
# CreateTime: 2021/5/11 20:39
# Summary: ''


# from mapper import db
from gino import Gino
from sqlalchemy import *

db = Gino()


class ForecastUserDO(db.Model):
    __tablename__ = 'forecast_user'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.CHAR(32), index=True, nullable=False)
    userPhone = db.Column(db.CHAR(32), index=True, nullable=False)
    userPassword = db.Column(db.CHAR(32))
    userName = db.Column(db.VARCHAR(64))
    userBirthday = db.Column(db.DateTime())
    userEmail = db.Column(db.VARCHAR(128))
    userSex = db.Column(db.SMALLINT(), default=0)
    userLoginTime = db.Column(db.DateTime())
    userCreateTime = db.Column(db.DateTime())
    userUpdateTime = db.Column(db.DateTime())
    userDelete = db.Column(db.SMALLINT(), default=0)
    userStatus = db.Column(db.SMALLINT(), default=0)
    userDisable = db.Column(db.SMALLINT(), default=0)
    userVIP = db.Column(db.SMALLINT(), default=0)


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