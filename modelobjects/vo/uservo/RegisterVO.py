# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: RegisterVO
# CreateTime: 2021/7/2 13:28
# Summary: ''


import uuid
import datetime

import pbkdf2


class RegisterVO(object):

    def __init__(self):
        self.__userId = uuid.uuid4().__str__()
        self.__userPhone = None
        self.__userName = None
        self.__userPassword = None
        self.__userBirthday = None
        self.__userEmail = None
        self.__userSex = 1
        self.__userLoginTime = None
        self.__createTime = datetime.datetime.now()
        self.__updateTime = None
        self.__userDelete = 0
        self.__userStatus = 1
        self.__userDisable = 0
        self.__userVIP = 1
        self.__userSource = 0

    def _hash_password(self, password):
        """
        @Author: SAM
        @CreateTime: 2021/7/13 13:59
        @UpdateTime(upf): 2021/7/13 13:59
        @Desc: '密码加密'
        """
        return pbkdf2.crypt(password, iterations=0x2537)

    @property
    def userId(self):
        return self.__userId

    # @userId.setter
    # def userId(self, value):
    #     self.__userId = value

    @property
    def userPhone(self):
        return self.__userPhone

    @userPhone.setter
    def userPhone(self, value):
        self.__userPhone = value

    @property
    def userName(self):
        return self.__userName

    @userName.setter
    def userName(self, value):
        self.__userName = value

    @property
    def userPassword(self):
        return self.__userPassword

    @userPassword.setter
    def userPassword(self, value):
        self.__userPassword = self._hash_password(value)

    @property
    def userBirthday(self):
        return self.__userBirthday

    @userBirthday.setter
    def userBirthday(self, value):
        self.__userBirthday = value

    @property
    def userEmail(self):
        return self.__userEmail

    @userEmail.setter
    def userEmail(self, value):
        self.__userEmail = value

    @property
    def userSex(self):
        return self.__userSex

    @userSex.setter
    def userSex(self, value):
        self.__userSex = value

    @property
    def userLoginTime(self):
        return self.__userLoginTime

    @userLoginTime.setter
    def userLoginTime(self, value):
        self.__userLoginTime = value

    @property
    def createTime(self):
        return self.__createTime

    # @createTime.setter
    # def createTime(self, value):
    #     self.__createTime = value

    @property
    def updateTime(self):
        return self.__updateTime

    @updateTime.setter
    def updateTime(self, value):
        self.__updateTime = value

    @property
    def userDelete(self):
        return self.__userDelete

    @userDelete.setter
    def userDelete(self, value):
        self.__userDelete = value

    @property
    def userStatus(self):
        return self.__userStatus

    @userStatus.setter
    def userStatus(self, value):
        self.__userStatus = value

    @property
    def userDisable(self):
        return self.__userDisable

    @userDisable.setter
    def userDisable(self, value):
        self.__userDisable = value

    @property
    def userSource(self):
        return self.__userSource

    @userSource.setter
    def userSource(self, value):
        self.__userSource = value
