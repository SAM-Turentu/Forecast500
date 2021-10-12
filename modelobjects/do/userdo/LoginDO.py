# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: LoginDO
# CreateTime: 2021/7/14 10:26
# Summary: ''


from backend.utils.Paginate import Pagination


class LoginDO:

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/14 10:26
        @UpdateTime(upf): 2021/7/14 10:26
        @Desc: ''
        """

        self.userPhone = None
        self.userPassword = None
        self.SMSCode = None

        self.userId = None
        self.userName = None
        self.userBirthday = None
        self.userEmail = None
        self.userSex = None
        self.userLoginTime = None
        self.userDelete = None
        self.userStatus = None
        self.userDisable = None
        self.userVIP = None
        self.userSource = None


class LoginInputDO:

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/21 13:03
        @UpdateTime(upf): 2021/7/21 13:03
        @Desc: ''
        """
        self.userPhone = None
        self.userPassword = None
        self.SMSCode = None


class OutputListDO(object):

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/23 16:24
        @UpdateTime(upf): 2021/7/23 16:24
        @Desc: '输出 list 基类'
        """
        self.data = []
        self.DO = self.DO if self.DO else None
        self.pagination = self.pagination if self.pagination else Pagination()()


class OutputDictDO(object):

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/23 16:25
        @UpdateTime(upf): 2021/7/23 16:25
        @Desc: '输出 dict 基类'
        """
        self.data = {}
        self.DO = self.DO if self.DO else None


class LoginOutputList(OutputListDO):
    """
    登录信息输出
    """

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/23 11:07
        @UpdateTime(upf): 2021/7/23 11:07
        @Desc: ''
        """
        # self.login_data = []  # peewee query data is not class-object !!!

        # todo 未完成
        self.DO = LoginOutputDO()
        self.pagination = Pagination()()
        super(LoginOutputList, self).__init__()


class LoginOutputDict(OutputDictDO):

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/27 16:04
        @UpdateTime(upf): 2021/7/27 16:04
        @Desc: ''
        """
        self.DO = LoginOutputDO()
        super(LoginOutputDict, self).__init__()


class LoginOutputDO:

    def __init__(self, *args, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/7/21 13:03
        @UpdateTime(upf): 2021/7/21 13:03
        @Desc: '登录输出信息'
        """
        # self.data = []
        self.userPhone = None
        # self.userPassword = None  # 输出 DO 不显示密码

        self.userId = None
        self.userName = None
        self.userBirthday = None
        self.userEmail = None
        self.userSex = None
        self.userLoginTime = None
        # self.userDelete = None
        self.userStatus = None
        self.userDisable = None
        self.userVIP = None
        self.userSource = None
