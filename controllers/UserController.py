# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserController
# CreateTime: 2021/5/17 20:41
# Summary: ''


from backend.core.Basehandler import BaseHandler
from backend.core.RouteHandler import Route
from backend.utils.Decorate import Return, CheckFrom
from forms.formfield.RegisterForm import RegisterForm
from modelobjects.ModelHelper import ModelHelper
from modelobjects.dto.userdto.RegisterDTO import RegisterDTO
from service.UserService import UserService
from vo.UserVO import RegisterVO


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
        """
        视图层 VO(View Object)

        需要将 VO 转为 DTO(Data Transfer Object) 传递给 服务层
        """
        self.form: RegisterVO  # 此处转为 DTO ？？
        dto = RegisterDTO()
        service = UserService()
        ModelHelper.VOTransferDTO(self.form, dto)
        return await service.register_user(dto)


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
