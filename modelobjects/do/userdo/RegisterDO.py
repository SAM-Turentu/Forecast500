# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: RegisterDO
# CreateTime: 2021/7/2 14:13
# Summary: ''


class RegisterDO:

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/2 14:13
        @UpdateTime(upf): 2021/7/2 14:13
        @Desc: ''
        """
        self.userId = None
        self.userPhone = None
        self.userName = None
        self.userPassword = None  # 业务逻辑，不能出现 password
        self.userBirthday = None
        self.userEmail = None
        self.userSex = None
        self.userLoginTime = None
        self.createTime = None
        self.updateTime = None
        self.userDelete = None
        self.userStatus = None
        self.userDisable = None
        self.userSource = None


class RegisterInputDO:

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/20 17:06
        @UpdateTime(upf): 2021/7/20 17:06
        @Desc: ''
        """
        self.userId = None
        self.userPhone = None
        self.userName = None
        self.userPassword = None
        self.userBirthday = None
        self.userEmail = None
        self.userSex = None
        self.userLoginTime = None
        self.createTime = None
        self.updateTime = None
        self.userDelete = None
        self.userStatus = None
        self.userDisable = None
        self.userSource = None
