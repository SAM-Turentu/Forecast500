# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseForm
# CreateTime: 2021/6/9 14:13
# Summary: ''


class BaseForm:

    def __init__(self, required=True, error_dict: dict = {}):
        """
        @author: SAM
        @CreateTime: 2021/6/9 17:11
        @UpdateTime(upf): 2021/6/9 17:11
        @desc: ''
        """
        self.required = required
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)

    def validate(self):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:16
        @UpdateTime(upf): 2021/6/9 14:16
        @desc: ''
        """


class String(BaseForm):

    def __init__(self, required=True, length: list = [0, 0], success_dict: dict = {}, error_dict: dict = {}):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:16
        @UpdateTime(upf): 2021/6/9 14:16
        @desc: ''
        """
        self.STRING = '^.*$'
        self.TEXT = '^[\s\S]*$'
        self.IP = '^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'
        self.EMAIL = '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
        self.PHONE = '^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$'
        self.required = required
        self.length = length
        self.min_length = None
        self.max_length = None

        # self.success_dict = {}

        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)

        self.is_valid = False
        self.value = None
        self.error = None

        super(BaseForm, String).__init__(required, length, error_dict)

    def validate(self):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:44
        @UpdateTime(upf): 2021/6/9 14:44
        @desc: ''
        """
        if len(self.length) == 1:
            self.min_length = 0
            self.max_length = self.length[0]
        elif len(self.length) == 2:
            if self.length[0] < self.length[1]:
                self.min_length = self.length[0]
                self.max_length = self.length[1]
            else:
                self.min_length = self.length[1]
                self.max_length = self.length[2]

    def check_length(self, length: list = None):
        """
        @author: SAM
        @CreateTime: 2021/6/9 16:07
        @UpdateTime(upf): 2021/6/9 16:07
        @desc: ''
        """


class Text(BaseForm):
    ...


class Integer(BaseForm):
    ...


class Float(BaseForm):
    ...


class Bool(BaseForm):
    ...


class DateTime(BaseForm):
    ...


class File(BaseForm):
    ...


class DataRequired:
    ...
