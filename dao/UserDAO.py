# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserDAO
# CreateTime: 2021/5/16 18:57
# Summary: '用户数据层'


from backend.utils.Decorate import NotExistException
from dao.BaseDAO import BaseDAO
from mapper.ForecastUserModel import ForecastUserModel


class UserDAO(BaseDAO):

    async def add_user(self, userPO):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/16 18:58
        @updateTime(upf): 2021/5/16 18:58
        """
        # todo 将服务层的 DO 转为 PO（持久化对象）
        # kw = {
        #     'userId': userPO.userId,
        #     'userPhone': userPO.userPhone,
        #     'userName': userPO.userName,
        #     'userPassword': None,
        #     'userBirthday': None,
        #     'userEmail': None,
        #     'userSex': 1,
        #     'userLoginTime': None,
        #     'createTime': None,
        #     'updateTime': None,
        #     'userDelete': 1,
        #     'userStatus': 1,
        #     'userDisable': 1,
        #     'userVIP': 1,
        # }
        await self.mysql.objects.create(ForecastUserModel, **userPO)

    @NotExistException
    async def query_user_list(self):
        """
        @func name: 
        @desc: 
        @author: SAM
        @createTime: 2021/5/16 20:12
        @updateTime(upf): 2021/5/16 20:12
        """
        data = await self.mysql.objects.execute(ForecastUserModel.select().paginate(1, 1).dicts())
        _ret = []
        # counts = data.__dict__.get('_result_wrapper').__dict__.get('count')
        for item in data:
            _ret.append(item)
        return _ret

    # @NotExistException
    async def login(self, loginPO):
        """
        @Author: SAM
        @CreateTime: 2021/7/16 9:47
        @UpdateTime(upf): 2021/7/16 9:47
        @Desc: ''
        """
        data = await self.mysql.objects.get(ForecastUserModel.select().where(
            ForecastUserModel.userPhone == loginPO.userPhone
        ).dicts())
        return data

    # @NotExistException
    async def query_user_by_phone(self, loginPO):
        """
        @Author: SAM
        @CreateTime: 2021/7/19 15:17
        @UpdateTime(upf): 2021/7/19 15:17
        @Desc: '根据手机号查询用户'
        """

        data = await self.mysql.objects.get(ForecastUserModel.select().where(
            ForecastUserModel.userPhone == loginPO.userPhone,
            ForecastUserModel.userStatus == 1,
            ForecastUserModel.userDelete == 0,
            ForecastUserModel.userDisable == 0,
        ).dicts())
        return data

    # @NotExistException
    async def auth_user_password(self, loginPO):
        """
        @Author: SAM
        @CreateTime: 2021/7/19 15:26
        @UpdateTime(upf): 2021/7/19 15:26
        @Desc: '核验密码'
        """
        data = await self.mysql.objects.get(ForecastUserModel.select().where(
            ForecastUserModel.userPhone == loginPO.userPhone
        ))
        boo = data.check_password(loginPO.userPassword)
        return boo
