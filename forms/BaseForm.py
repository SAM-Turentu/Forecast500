# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseForm
# CreateTime: 2021/6/9 14:13
# Summary: ''


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
        self.value = None
        self.field_name = FieldName()
        self.field_name.label = label  # 不能为空
        self.flag = True
        self.success = {}
        self.error = {}
        self.message = message  # 错误提示
        self.validators = validators

    def validate(self):
         """
        @author: SAM
        @CreateTime: 2021/6/9 14:16
        @UpdateTime(upf): 2021/6/9 14:16
        @desc: ''
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
        _pattern = re.compile(pattern)
        _match = _pattern.match(self.value)
        if _match:
            self.success.update({
                self.field_name.en_name: self.value
            })
        else:
            self.flag = False
            message = self.message if self.message else 'Matching error occurred!'
            if self.error.get(self.field_name.en_name):
                self.error.get(self.field_name.en_name).append(message)
            else:
                self.error[self.field_name.en_name] = [message]


class String(BaseForm):

    def __init__(self, required=True, length: list = [0, 0], success_dict: dict = {}, error_dict: dict = {}):
        """
        @Author: SAM
        @CreateTime: 2021/6/9 14:16
        @UpdateTime(upf): 2021/6/9 14:16
        @Desc: ''
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

    def validate(self, value=None):
        """
        @author: SAM
        @CreateTime: 2021/6/9 14:44
        @UpdateTime(upf): 2021/6/18 17:25
        @desc: ''
        """
        self.value = value
        self.call_validators()

        self.match_input(self.STRING)
        return self


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
