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
from backend.utils.Decorate import Return, CheckFrom
from forms.formfield.RegisterForm import RegisterForm
from service.UserService import UserService
from vo.RegisterVO import RegisterVO


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
    @CheckFrom(RegisterForm(), RegisterVO())
    async def post(self):
        self.form: RegisterVO
        userName = self.form.userName
        userPhone = self.form.userPhone
        password = self.form.password
        userId = uuid.uuid4().__str__()
        service = UserService()
        return await service.register_user(userId=userId, userName=userName, userPhone=userPhone, password=password)


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
