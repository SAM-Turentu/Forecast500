# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserPO
# CreateTime: 2021/7/6 16:21
# Summary: ''


class UserPO:

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/6 16:21
        @UpdateTime(upf): 2021/7/6 16:21
        @Desc: ''
        """
        self.userId: str = ''
        self.userPhone: str = ''
        self.userName: str = ''
        self.userPassword: str = ''
        self.userBirthday = None
        self.userEmail: str = ''
        self.userSex: int = 0
        self.userLoginTime = None
        self.createTime = None
        self.updateTime = None
        self.userDelete: int = 0
        self.userStatus: int = 0
        self.userDisable: int = 0
        self.userVIP: int = 0
        self.userSource: int = 0
        assert type(self.userId) is str
        assert type(self.userPhone) is str
        assert type(self.userName) is str
        assert type(self.userPassword) is str

        # assert type(self.userBirthday) is str

        assert type(self.userEmail) is str
        assert type(self.userSex) is int

        # assert type(self.userLoginTime) is str
        # assert type(self.createTime) is str
        # assert type(self.updateTime) is str

        assert type(self.userDelete) is int
        assert type(self.userStatus) is int
        assert type(self.userDisable) is int
        assert type(self.userVIP) is int
        assert type(self.userSource) is int
