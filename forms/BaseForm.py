# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseForm
# CreateTime: 2021/6/9 14:13
# Summary: ''


import re


class FieldName:
    label = None
    en_name = None


class BaseForm:

    def __init__(self, label: str, message=None, validators: list = None):
        """
        @Author: SAM
        @CreateTime: 2021/6/9 17:11
        @UpdateTime(upf): 2021/6/18 17:25
        @Desc: ''
        """
        self.values = None
        self.field_name = FieldName()
        self.field_name.label = label  # 不能为空
        self.flag = True
        self.success = {}
        self.error = {}
        self.message = message  # 错误提示
        self.validators = validators

    def validate(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/9 14:16
        @UpdateTime(upf): 2021/6/9 14:16
        @Desc: ''
        """

    def call_validators(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/18 16:51
        @UpdateTime(upf): 2021/6/18 16:51
        @Desc: ''
        """
        if self.validators:
            for validator in self.validators:
                if callable(validator):
                    validator(self)
                else:
                    raise Exception('This function cannot be called!')

    def match_input(self, pattern):
        """
        @Author: SAM
        @CreateTime: 2021/6/18 16:51
        @UpdateTime(upf): 2021/6/18 16:51
        @Desc: ''
        """
        if not self.values and self.values != 0:
            self.success.update({
                self.field_name.en_name: self.values
            })
            return
        _pattern = re.compile(pattern)
        _match = _pattern.match(self.values)
        if _match:
            self.success.update({
                self.field_name.en_name: self.values
            })
        else:
            self.flag = False
            message = self.message if self.message else 'Matching error occurred!'
            if self.error.get(self.field_name.en_name):
                self.error.get(self.field_name.en_name).append(message)
            else:
                self.error[self.field_name.en_name] = [message]


class String(BaseForm):

    # todo 待删除
    # def __init__(self, required=True, length: list = [0, 0], success_dict: dict = {}, error_dict: dict = {}):
    #     """
    #     @Author: SAM
    #     @CreateTime: 2021/6/9 14:16
    #     @UpdateTime(upf): 2021/6/9 14:16
    #     @Desc: ''
    #     """
    #     self.STRING = '^.*$'
    #     self.TEXT = '^[\s\S]*$'
    #     self.IP = '^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'
    #     self.EMAIL = '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
    #     self.PHONE = '^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$'
    #     self.required = required
    #
    #     # self.success_dict = {}
    #
    #     self.error_dict = {}
    #     if error_dict:
    #         self.error_dict.update(error_dict)
    #
    #     self.is_valid = False
    #     self.values = None
    #     self.error = None
    #
    #     super(BaseForm, String).__init__(required, length, error_dict)

    def validate(self, values=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/9 14:44
        @UpdateTime(upf): 2021/6/18 17:25
        @Desc: ''
        """
        self.values = values
        self.call_validators()
        pattern = '^.*$'
        self.match_input(pattern)
        return self

    def check_validate(self, values=None, pattern=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 14:28
        @UpdateTime(upf): 2021/6/22 14:28
        @Desc: ''
        """
        self.values = values
        self.call_validators()
        self.match_input(pattern)
        return self


# region Description
class Text(BaseForm):

    def validate(self, values=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:32
        @UpdateTime(upf): 2021/6/22 16:32
        @Desc: ''
        """
        self.values = values
        self.call_validators()
        pattern = '^[\s\S]*$'
        self.match_input(pattern)
        return self


class Integer(BaseForm):

    def validate(self, values=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:32
        @UpdateTime(upf): 2021/6/22 16:32
        @Desc: ''
        """
        self.values = values
        self.call_validators()
        pattern = ''
        self.match_input(pattern)
        return self


class Float(BaseForm):

    def validate(self, values=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:32
        @UpdateTime(upf): 2021/6/22 16:32
        @Desc: ''
        """
        self.values = values
        self.call_validators()
        pattern = ''
        self.match_input(pattern)
        return self


class Bool(BaseForm):

    def validate(self, values=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:32
        @UpdateTime(upf): 2021/6/22 16:32
        @Desc: ''
        """
        self.values = values
        self.call_validators()
        pattern = ''
        self.match_input(pattern)
        return self


class DateTime(BaseForm):

    def validate(self, values=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:32
        @UpdateTime(upf): 2021/6/22 16:32
        @Desc: ''
        """
        self.values = values
        self.call_validators()
        pattern = ''
        self.match_input(pattern)
        return self


class File(BaseForm):

    def validate(self, values=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:32
        @UpdateTime(upf): 2021/6/22 16:32
        @Desc: ''
        """
        self.values = values
        self.call_validators()
        pattern = ''
        self.match_input(pattern)
        return self


# endregion


class DataRequired:

    def __init__(self, message=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:37
        @UpdateTime(upf): 2021/6/22 16:37
        @Desc: ''
        """
        self.message = message

    def __call__(self, cls):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:37
        @UpdateTime(upf): 2021/6/22 16:37
        @Desc: ''
        """
        ''
        if not cls.values:
            cls.flag = False
            message = self.message if self.message else f'{cls.field_name.label} 为必填项'
            if cls.error.get(cls.field_name.en_name):
                cls.error.get(cls.field_name.en_name).append(message)
            else:
                cls.error[cls.ield_name.en_name] = [message]
        return cls  # type: BaseForm


class Length:

    def __init__(self, min_len=-1, max_len=-1, message=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:38
        @UpdateTime(upf): 2021/6/22 16:38
        @Desc: ''
        """
        assert min_len != -1 or max_len != -1, 'At least one of `min` or `max` must be specified.'
        assert max_len == -1 or min_len <= max_len, '`min` cannot be more than `max`.'
        self.min_len = min_len
        self.max_len = max_len
        self.message = message

    def __call__(self, cls):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:38
        @UpdateTime(upf): 2021/6/22 16:38
        @Desc: ''
        """
        if len(cls.values) < self.min_len:
            cls.flag = False
            message = self.message if self.message else f'{cls.field_name.label} 长度不足'
            if cls.error.get(cls.field_name.en_name):
                cls.error.get(cls.field_name.en_name).append(message)
            else:
                cls.error[cls.ield_name.en_name] = [message]
        if len(cls.values) > self.max_len:
            cls.flag = False
            message = self.message if self.message else f'{cls.field_name.label} 长度超出'
            if cls.error.get(cls.field_name.en_name):
                cls.error.get(cls.field_name.en_name).append(message)
            else:
                cls.error[cls.field_name.en_name] = [message]
        return cls


# todo 未完成
class NumofFile:

    def __init__(self, min_files=1, max_files=1, message=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:44
        @UpdateTime(upf): 2021/6/22 16:44
        @Desc: '限制上传文件数量'
        必传字段
        """
        self.min_files = min_files  # 文件最小数
        self.max_files = max_files  # 文件最大数
        self.message = message

    def __call__(self, cls):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:45
        @UpdateTime(upf): 2021/6/22 16:45
        @Desc: ''
        """
        # 必传字段
        # dataRequired = DataRequired(cls.message)
        # dataRequired(cls)
        if not cls.values:
            cls.flag = False
            message = self.message if self.message else f'缺少{cls.field_name.label}'  # 缺少文件
        else:
            if len(cls.values) > self.max_files:
                cls.flag = False
                message = self.message if self.message else f'{cls.field_name.label} 不能超过{self.max_files}个'  # 超过最大文件数

            elif len(cls.values) < self.min_files:
                cls.flag = False
                message = self.message if self.message else f'{cls.field_name.label} 不能少于{self.min_files}个'  # 低于最小文件数
            else:
                message = None

        if not cls.flag:
            if cls.error.get(cls.field_name.en_name):
                cls.error.get(cls.field_name.en_name).append(message)
            else:
                cls.error[cls.ield_name.en_name] = [message]
        return cls


# todo 未完成
class ContentLength:

    def __init__(self, min_len=-1, max_len=-1, message=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:45
        @UpdateTime(upf): 2021/6/22 16:45
        @Desc: ''
        """
        # tornado 默认最大文件不能超过 1024 * 1024 * 100  = 100MB
        self.max_buffer_size = 1024 * 1024 * 100  # CONF.settings.max_buffer_size
        assert min_len != -1 or max_len != -1, 'At least one of `min` or `max` must be specified.'
        assert max_len == -1 or min_len <= max_len, '`min` cannot be more than `max`.'
        assert max_len >= self.max_buffer_size, f'max cannot be more than `max_buffer_size({self.max_buffer_size} MB)`.'
        self.min_len = min_len
        self.max_len = max_len
        self.message = message

    def __call__(self, cls):
        """
        @Author: SAM
        @CreateTime: 2021/6/22 16:46
        @UpdateTime(upf): 2021/6/22 16:46
        @Desc: ''
        """
        if not cls.values:
            cls.flag = False
            # message = self.message if self.message else 'message'
            # cls.error.update({
            #     cls.field_name.en_name: message
            # })
        return cls
