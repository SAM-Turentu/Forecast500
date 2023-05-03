# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: MainForm
# CreateTime: 2021/6/9 14:15
# Summary: ''


from backend.utils.Utils import Utils
from forms.BaseForm import *


class MainForm:

    def check_valid(self, handler, vo):
        """
        @Author: SAM
        @CreateTime: 2021/6/9 14:14
        @UpdateTime(upf): 2021/6/9 14:14
        @Desc: ''
        """
        flag = True
        success_dict = {}
        error_dict = {}

        for key, forms in self.__dict__.items():
            forms.field_name.en_name = key
            if type(forms) is String:
                values = handler.get_argument(key, None)  # post
            elif type(forms) is File:
                values = handler.request.files.get(key, None)
            else:
                values = handler.get_argument(key, None)
            result = forms.validate(values=values)
            if result.flag:
                success_dict[key] = result.success[key]
            else:
                flag = False
                error_dict[key] = result.error[key]

        Utils.FormTransferVO(success_dict, vo)
        return flag, vo, error_dict

# region Annotation
# class StringField(String):
#
#     def validate(self):
#         """
#         @Author: SAM
#         @CreateTime: 2021/6/9 14:16
#         @UpdateTime(upf): 2021/6/9 14:16
#         @Desc: ''
#         """
#         self.check_validate(self.value, self.STRING)
#
#
# class TextField(String):
#
#     def validate(self, length: list = None):
#         """
#         @Author: SAM
#         @CreateTime: 2021/6/9 15:03
#         @UpdateTime(upf): 2021/6/9 15:03
#         @Desc: ''
#         """
#         self.check_validate(self.value, self.TEXT)
#
#
# class PhoneField(String):
#
#     def validate(self):
#         """
#         @Author: SAM
#         @CreateTime: 2021/6/9 14:18
#         @UpdateTime(upf): 2021/6/9 14:18
#         @Desc: ''
#         """
#
#
# class EmailField(String):
#
#     def validate(self):
#         """
#         @Author: SAM
#         @CreateTime: 2021/6/9 14:19
#         @UpdateTime(upf): 2021/6/9 14:19
#         @Desc: ''
#         """
# endregion
