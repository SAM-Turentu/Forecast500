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

    class Meta:
        table_name = 'forecast_user'


# class UserService:
#
#     async def add_user(self, userId=None, userPhone=None, userName=None):
#         """
#         @func name:
#         @desc:
#         @author: SAM
#         @createTime: 2021/5/11 22:15
#         @updateTime(upf): 2021/5/11 22:15
#         """
#         userId = uuid.uuid4().__str__()
#         userPhone = '18292007162'
#         userName = '土人土3'
#         kw = {
#             'userId': userId,
#             'userPhone': userPhone,
#             'userName': userName,
#             'userPassword': None,
#             'userBirthday': None,
#             'userEmail': None,
#             'userSex': 1,
#             'userLoginTime': None,
#             'createTime': None,
#             'updateTime': None,
#             'userDelete': 1,
#             'userStatus': 1,
#             'userDisable': 1,
#             'userVIP': 1,
#         }
#         await objects.create(ForecastUserDO, **kw)
#         data = await objects.execute(ForecastUserDO.select())
#         _ret = []
#         for item in data:
#             _ret.append({
#                 'userId': item.userId,
#                 'userPhone': item.userPhone,
#                 'userName': item.userName,
#             })
#         return ReturnJson.success(data=_ret)
