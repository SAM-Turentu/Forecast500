# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: UserLoginVO
# CreateTime: 2021/7/13 15:46
# Summary: ''


class UserLoginVO:

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/13 15:47
        @UpdateTime(upf): 2021/7/13 15:47
        @Desc: ''
        """
        self.__userPhone = None
        self.__userPassword = None
        self.__SMSCode = None

    @property
    def userPhone(self):
        return self.__userPhone

    @userPhone.setter
    def userPhone(self, value):
        self.__userPhone = value

    @property
    def userPassword(self):
        return self.__userPassword

    @userPassword.setter
    def userPassword(self, value):
        self.__userPassword = value

    @property
    def SMSCode(self):
        return self.__SMSCode

    @SMSCode.setter
    def SMSCode(self, value):
        self.__SMSCode = value
