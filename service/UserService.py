# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserService
# CreateTime: 2021/5/16 19:01
# Summary: ''


from backend.utils.Result import ReturnJson
from dao.UserDAO import UserDAO
from service.BaseService import BaseService


class UserService(BaseService):

    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/16 19:02
        @updateTime(upf): 2021/5/16 19:02
        """
        self.userDAO = UserDAO.getInstance()

    async def register_user(self, **kwargs):
        """
        @func name: 用户注册
        @desc:
        @author: SAM
        @createTime: 2021/5/16 19:03
        @updateTime(upf): 2021/5/16 19:03
        """
        _ret = await self.userDAO.add_user(**kwargs)
        return ReturnJson.success(data=_ret)

    async def query_user_list(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/17 19:51
        @updateTime(upf): 2021/5/17 19:51
        """
        _ret = await self.userDAO.query_user_list()
        return ReturnJson.success(data=_ret)
