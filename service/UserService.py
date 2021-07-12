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
from modelobjects.do.userdo.RegisterDO import RegisterDO
from modelobjects.dto.userdto.RegisterDTO import RegisterDTO
from modelobjects.po.UserPO import UserPO
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

        # DO 初始化
        registerDO = RegisterDO()

        # DTO to DO
        ModelHelper.DTOTransferDO(dto, registerDO)

        # DO 做逻辑处理
        registerDO.userId = uuid.uuid4().__str__()
        registerDO.userSex = 1 if registerDO.userSex == '男' else 2 if registerDO.userSex == '女' else 0

        # DTO 和 DO 字段名不同的需要手动赋值
        registerDO.user_name = dto.userName

        # DO 可以忽略 DTO 中部分数据

        # DO 返回给展示层的数据中，可只传递部分数据

        # DO 和 PO 一一对应
        registerPO = UserPO()

        # DO to PO
        ModelHelper.DOTransferPO(registerDO, registerPO)  # DO 和 PO 字段名称几乎一致
        # DO 和 PO 多对多的关系（多对一比较常见）

        # 将 PO 传入下方 持久化方法中

        _ret = await self.userDAO.add_user(registerPO.__dict__)
        return ReturnJson.SUCCESS(data=_ret)
        # return ReturnJson.SUCCESS(data={'_ret': True, 'userPhone': form.userPhone, 'userName': form.userName})

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
