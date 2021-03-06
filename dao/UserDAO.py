# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserDAO
# CreateTime: 2021/5/16 18:57
# Summary: '用户数据层'


from dao.BaseDAO import BaseDAO
from mapper.ForecastUserDO import ForecastUserDO


class UserDAO(BaseDAO):

    async def add_user(self, userId, userPhone, userName):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/16 18:58
        @updateTime(upf): 2021/5/16 18:58
        """
        kw = {
            'userId': userId,
            'userPhone': userPhone,
            'userName': userName,
            'userPassword': None,
            'userBirthday': None,
            'userEmail': None,
            'userSex': 1,
            'userLoginTime': None,
            'createTime': None,
            'updateTime': None,
            'userDelete': 1,
            'userStatus': 1,
            'userDisable': 1,
            'userVIP': 1,
        }
        await self.mysql.objects.create(ForecastUserDO, **kw)

    async def query_user_list(self):
        """
        @func name: 
        @desc: 
        @author: SAM
        @createTime: 2021/5/16 20:12
        @updateTime(upf): 2021/5/16 20:12
        """
        data = await self.mysql.objects.execute(ForecastUserDO.select().dicts())
        _ret = []
        for item in data:
            _ret.append(item)
            # _ret.append({
            #     'userId': item['userId'],
            #     'userPhone': item['userPhone'],
            #     'userName': item['userName'],
            #     'create': item['createTime'],
            # })
        return _ret
