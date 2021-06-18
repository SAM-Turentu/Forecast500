# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: MainForm
# CreateTime: 2021/6/9 14:15
# Summary: ''


from forms.BaseForm import String


class MainForm:

    def __init__(self):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:13
        @UpdateTime(upf): 2021/6/9 14:13
        @desc: ''
        """

    def check_valid(self, handler):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:14
        @UpdateTime(upf): 2021/6/9 14:14
        @desc: ''
        """


# region Description
class StringField(String):

    def validate(self):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:16
        @UpdateTime(upf): 2021/6/9 14:16
        @desc: ''
        """


class TextField(String):

    def validate(self, length: list = None):
        """
        @author: SAM
        @CreateTime: 2021/6/9 15:03
        @UpdateTime(upf): 2021/6/9 15:03
        @desc: ''
        """


class PhoneField(String):

    def validate(self):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:18
        @UpdateTime(upf): 2021/6/9 14:18
        @desc: ''
        """


class EmailField(String):

    def validate(self):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:19
        @UpdateTime(upf): 2021/6/9 14:19
        @desc: ''
        """
# endregion
