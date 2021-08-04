# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserService
# CreateTime: 2021/5/16 19:01
# Summary: ''


import uuid
from backend.utils.BaseReturn import ReturnJson
from dao.UserDAO import UserDAO
from modelobjects.ModelHelper import ModelHelper
from modelobjects.do.userdo.LoginDO import LoginDO, LoginOutputDO
from modelobjects.po.userpo.LoginPO import LoginPO
from modelobjects.do.userdo.RegisterDO import RegisterDO
from modelobjects.dto.userdto.LoginDTO import LoginDTO
from modelobjects.dto.userdto.RegisterDTO import RegisterDTO
from modelobjects.po.userpo.UserPO import UserPO
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

        """
        服务层需要 DO，用 DO 完成逻辑业务
        """

    async def register_user(self, dto: RegisterDTO):
        """
        @func name: 用户注册
        @desc:
        @author: SAM
        @createTime: 2021/5/16 19:03
        @updateTime(upf): 2021/5/16 19:03
        """

        """
        服务层需要将 DTO 重新构造成 DO(Domain Object)，调用 DO 完成具体业务
        
        最后把 DO 转为 PO(Persistent Object) 传给持久层
        """

        """
        DTO to DO
        
        DO 逻辑处理
        
        DO to PO
        """
        registerDO = RegisterDO()
        # DTO to DO
        ModelHelper.DTOTransferDO(dto, registerDO)

        """
        DTO 和 DO 字段名不同的需要手动赋值
        
        DO 可以忽略 DTO 中部分数据
        
        DO 返回给展示层的数据中，可只传递部分数据
        """

        # DO 做逻辑处理
        registerDO.userId = uuid.uuid4().__str__()
        # 0:'隐匿'; 1:'男', '先生', '帅哥', '小伙子'; 2:'女', '女士', '美女', '小姑娘'
        registerDO.userSex = 1 if registerDO.userSex in ['男', '先生', '帅哥', '小伙子'] else 2 if registerDO.userSex == ['女', '女士', '美女', '小姑娘'] else 0
        registerDO.user_name = dto.userName

        registerPO = UserPO()
        # DO to PO
        ModelHelper.DOTransferPO(registerDO, registerPO)  # DO 和 PO 字段名称几乎一致

        """
        
        DO 和 PO 多对多的关系（多对一比较常见）
        
        将 PO 传入下方 持久化方法中
        
        """

        _ret = await self.userDAO.add_user(registerPO.__dict__)
        # todo 将返回放置在 控制器中
        return ReturnJson.SUCCESS(data=_ret)

    async def query_user_list(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/17 19:51
        @updateTime(upf): 2021/5/17 19:51
        """
        _ret = await self.userDAO.query_user_list()
        return ReturnJson.SUCCESS(data=_ret)

    async def user_login(self, dto: LoginDTO):
        """
        @Author: SAM
        @CreateTime: 2021/7/13 16:47
        @UpdateTime(upf): 2021/7/13 16:47
        @Desc: ''
        """

        loginDO = LoginDO()
        ModelHelper.DTOTransferDO(dto, loginDO)

        SMSCode = '101010'  # redis:sms_code

        if loginDO.SMSCode != SMSCode and loginDO.SMSCode != '':
            return ReturnJson.FAILURE(error_message='请填写正确的验证码!')

        if loginDO.userPassword:
            ...

        loginPO = LoginPO()

        ModelHelper.DOTransferPO(loginDO, loginPO)

        _ret = await self.userDAO.login(loginPO)

        # 检查账号是否存在
        is_user = await self.userDAO.login(loginPO)
        if not is_user:
            # 用户不存在
            # todo 用户若不存在，可直接注册（注册登录合并？）？
            return ReturnJson.NOTFIND(message='用户不存在!', code=204, redirect='/register')

        # 检查密码是否正确
        is_password = await self.userDAO.auth_user_password(loginPO)
        if not is_password:
            # 密码不正确
            return ReturnJson.FAILURE(error_message='密码不正确，请重新输入!')

        # 测试
        # _ret = await self.userDAO.query_user_list()

        loginOutputDO = LoginOutputDO()

        # is_user 转换为 DO
        ModelHelper.DataTransferDO(_ret, loginOutputDO)
        # ModelHelper.DataTransferDO(is_user, loginDO)

        # 0:'隐匿'; 1:'男', '先生', '帅哥', '小伙子'; 2:'女', '女士', '美女', '小姑娘'
        # loginDO.userSex = '帅哥' if is_user.userSex == 1 else '美女' if is_user.userSex == 2 else '隐匿'

        # loginDO.userId = is_user.userId
        # loginDO.userPhone = is_user.userPhone
        # loginDO.userName = is_user.userName
        # loginDO.userBirthday = is_user.userBirthday
        # loginDO.userEmail = is_user.userEmail
        # loginDO.userSex = is_user.userSex
        # loginDO.userLoginTime = is_user.userLoginTime
        # loginDO.userDelete = is_user.userDelete
        # loginDO.userStatus = is_user.userStatus
        # loginDO.userDisable = is_user.userDisable
        # loginDO.userVIP = is_user.userVIP
        # loginDO.userSource = is_user.userSource

        return ReturnJson.SUCCESS(data=loginOutputDO.data)
