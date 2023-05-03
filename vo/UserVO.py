# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserVO
# CreateTime: 2021/6/23 13:23
# Summary: ''


# todo 可修改为form表单校验


import datetime
import pbkdf2


# from pbkdf2 import PBKDF2, crypt


class RegisterVO_Test(object):

    def __init__(self):
        self._userId = None
        self._userPhone = None
        self._userName = None
        self._userPassword = None
        self._userBirthday = None
        self._userEmail = None
        self._userSex = 1
        self._userLoginTime = None
        self._createTime = datetime.datetime.now()
        self._updateTime = None
        self._userDelete = 0
        self._userStatus = 1
        self._userDisable = 0
        self._userVIP = 1
        self._userSource = None

    def _hash_password(self, password):
        """
        @Author: SAM
        @CreateTime: 2021/7/13 13:59
        @UpdateTime(upf): 2021/7/13 13:59
        @Desc: '密码加密'
        """
        return pbkdf2.crypt(password, iterations=0x2537)

    # def auth_password(self, pwd):
    #     """
    #     @Author: SAM
    #     @CreateTime: 2021/7/13 14:30
    #     @UpdateTime(upf): 2021/7/13 14:30
    #     @Desc: ''
    #     """
    #     if self.userPassword is not None:
    #         return self.userPassword == pbkdf2.crypt(pwd, self.userPassword)
    #     else:
    #         return False

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, value):
        self._userId = value

    @property
    def userPhone(self):
        return self._userPhone

    @userPhone.setter
    def userPhone(self, value):
        self._userPhone = value

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self, value):
        self._userName = value

    @property
    def userPassword(self):
        return self._userPassword

    @userPassword.setter
    def userPassword(self, value):
        self._userPassword = self._hash_password(value)

    @property
    def userBirthday(self):
        return self._userBirthday

    @userBirthday.setter
    def userBirthday(self, value):
        self._userBirthday = value

    @property
    def userEmail(self):
        return self._userEmail

    @userEmail.setter
    def userEmail(self, value):
        self._userEmail = value

    @property
    def userSex(self):
        return self._userSex

    @userSex.setter
    def userSex(self, value):
        self._userSex = value

    @property
    def userLoginTime(self):
        return self._userLoginTime

    @userLoginTime.setter
    def userLoginTime(self, value):
        self._userLoginTime = value

    @property
    def createTime(self):
        return self._createTime

    @createTime.setter
    def createTime(self, value):
        self._createTime = value

    @property
    def updateTime(self):
        return self._updateTime

    @updateTime.setter
    def updateTime(self, value):
        self._updateTime = value

    @property
    def userDelete(self):
        return self._userDelete

    @userDelete.setter
    def userDelete(self, value):
        self._userDelete = value

    @property
    def userStatus(self):
        return self._userStatus

    @userStatus.setter
    def userStatus(self, value):
        self._userStatus = value

    @property
    def userDisable(self):
        return self._userDisable

    @userDisable.setter
    def userDisable(self, value):
        self._userDisable = value

    @property
    def userSource(self):
        return self._userSource

    @userSource.setter
    def userSource(self, value):
        self._userSource = value
