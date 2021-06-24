# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserController
# CreateTime: 2021/5/17 20:41
# Summary: ''


import uuid
from backend.core.Basehandler import BaseHandler
from backend.core.RouteHandler import Route
from backend.utils.Decorate import Return
from forms.formfield.RegisterForm import RegisterForm
from service.UserService import UserService
from vo.RegisterVO import RegisterVO


@Route('/reg')
class registerHandler(BaseHandler):

    @Return
    async def post(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/23 16:40
        @UpdateTime(upf): 2021/6/23 16:40
        @Desc: ''
        """
        print(123)


@Route('/register')
class RegisterUserHandler(BaseHandler):
    """
    @interface name: 用户注册
    @desc:
    @author: SAM
    @createTime: 2021/5/11 22:17
    @updateTime(upf): 2021/5/11 22:17
    """

    @Return
    async def post(self):
        obj = RegisterForm()
        flag, success, error = obj.check_valid(self, vo=RegisterVO())
        result = {'flag': flag, 'success': success, 'error': error}
        if not flag:
            return self.write({'result': result})

        userId = uuid.uuid4().__str__()
        userPhone = self.get_body_argument('userPhone', None)
        userName = self.get_body_argument('userName', None)
        password = self.get_body_argument('password', None)
        service = UserService()
        return await service.register_user(userId=userId, userName=userName, userPhone=userPhone)


@Route('/getUsers')
class getUserListHandler(BaseHandler):
    """
    @interface name: 获取用户列表
    @desc:
    @author: SAM
    @createTime: 2021/5/17 19:52
    @updateTime(upf): 2021/5/17 19:52
    """

    @Return
    async def get(self):
        service = UserService()
        return await service.query_user_list()
