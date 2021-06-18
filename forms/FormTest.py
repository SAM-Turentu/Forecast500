# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: FormTest
# CreateTime: 2021/6/10 13:19
# Summary: ''


import re
from typing import Any
import tornado.web
import tornado.ioloop


class FieldName:
    label = None
    en_name = None


class BaseForm:

    def __init__(self, label: str, message=None, validators: list = None):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:19
        @UpdateTime(upf): 2021/6/10 13:19
        @desc: ''
        """
        self.value = None
        self.field_name = FieldName()
        self.field_name.label = label  # 不能为空
        self.flag = True
        self.success = {}
        self.error = {}
        self.message = message  # 错误提示
        self.validators = validators

    def check_validate(self):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:19
        @UpdateTime(upf): 2021/6/10 13:19
        @desc: '所有类都继承该方法'
        """
        ...

    def call_validators(self):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:35
        @UpdateTime(upf): 2021/6/10 13:35
        @desc: ''
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
        @CreateTime: 2021/6/18 13:00
        @UpdateTime(upf): 2021/6/18 13:00
        @Desc: '正则匹配'
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

    def check_validate(self, value=None):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:20
        @UpdateTime(upf): 2021/6/10 13:20
        @desc: ''
        """
        self.value = value
        self.call_validators()  # 先执行附加条件，flag = False 不在继续执行下面方法
        # if not self.flag:
        #     return self

        pattern = '^.*$'
        self.match_input(pattern)

        return self


class Float(BaseForm):

    def check_validate(self, value=None):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:20
        @UpdateTime(upf): 2021/6/10 13:20
        @desc: ''
        """
        self.value = value
        self.call_validators()
        if not self.flag:
            return self
        pattern = ''
        self.match_input(pattern)
        return self


class Text(BaseForm):

    def check_validate(self, value=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/18 14:24
        @UpdateTime(upf): 2021/6/18 14:24
        @Desc: ''
        """
        self.value = value
        self.call_validators()
        if not self.flag:
            return self
        pattern = '^[\s\S]*$'
        self.match_input(pattern)
        return self


class DateRequired:

    def __init__(self, message):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:25
        @UpdateTime(upf): 2021/6/10 13:25
        @desc: ''
        """
        self.message = message

    def __call__(self, cls):
        """
        @author: SAM
        @CreateTime: 2021/6/17 17:22
        @UpdateTime(upf): 2021/6/17 17:22
        @desc: ''
        """
        if not cls.value:
            cls.flag = False
            message = self.message if self.message else f'{cls.field_name.label} 为必填项'
            if cls.error.get(cls.field_name.en_name):
                cls.error.get(cls.field_name.en_name).append(message)
            else:
                cls.error[cls.ield_name.en_name] = [message]
        return cls


class Length:

    def __init__(self, min_len=-1, max_len=-1, message=None):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:25
        @UpdateTime(upf): 2021/6/10 13:25
        @desc: ''
        """
        assert min_len != -1 or max_len != -1, 'At least one of `min` or `max` must be specified.'
        assert max_len == -1 or min_len <= max_len, '`min` cannot be more than `max`.'
        self.min_len = min_len
        self.max_len = max_len
        self.message = message

    def __call__(self, cls):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:28
        @UpdateTime(upf): 2021/6/10 13:28
        @desc: ''
        """
        if len(cls.value) < self.min_len:
            cls.flag = False
            message = self.message if self.message else f'{cls.field_name.label} 长度不足'
            if cls.error.get(cls.field_name.en_name):
                cls.error.get(cls.field_name.en_name).append(message)
            else:
                cls.error[cls.ield_name.en_name] = [message]
        if len(cls.value) > self.max_len:
            cls.flag = False
            message = self.message if self.message else f'{cls.field_name.label} 长度超出'
            if cls.error.get(cls.field_name.en_name):
                cls.error.get(cls.field_name.en_name).append(message)
            else:
                cls.error[cls.ield_name.en_name] = [message]
        return cls


class MainForm:

    def check_valid(self, handler):
        """
        @author: SAM
        @CreateTime: 2021/6/10 15:23
        @UpdateTime(upf): 2021/6/10 15:23
        @desc: ''
        """
        flag = True
        success_dict = {}
        error_dict = {}

        for key, validator in self.__dict__.items():
            value = handler.get_query_argument(key)

            validator.field_name.en_name = key

            if type(validator) is String:
                # 此处调用校验器
                result = validator.check_validate(value=value)

                if result.flag:
                    success_dict[key] = result.success[key]
                else:
                    flag = False
                    error_dict[key] = result.error[key]

        return flag, success_dict, error_dict


class MainTestForm(MainForm):
    """
    @author: SAM
    @CreateTime: 2021/6/10 13:29
    @UpdateTime(upf): 2021/6/10 13:29
    @desc: ''
    """

    def __init__(self):
        """
        @author: SAM
        @CreateTime: 2021/6/10 16:57
        @UpdateTime(upf): 2021/6/10 16:57
        @desc: ''
        """
        self.name = String(label='姓名', validators=[DateRequired('Hello world!'), Length(1, 10, 'check string length.')])


# region Description
class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        """
        @author: SAM
        @CreateTime: 2021/6/15 12:51
        @UpdateTime(upf): 2021/6/15 12:51
        @desc: ''
        """
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        """
        @author: SAM
        @CreateTime: 2021/6/16 11:06
        @UpdateTime(upf): 2021/6/16 11:06
        @desc: ''
        """
        exc_cls, exc_instance, trace = kwargs.get('exc_info')
        if status_code != 200:
            self.set_status(status_code)
            self.write(exc_instance.__str__())

    def ValidateForm(self, form):
        """
        @author: SAM
        @CreateTime: 2021/6/15 12:53
        @UpdateTime(upf): 2021/6/15 12:53
        @desc: ''
        """
        if callable(form):
            obj = form()
            flag, success, error = obj.check_valid(self)
            result = {'flag': flag, 'success': success, 'error': error}
            if not flag:
                self.write({'result': result})
                # raise Exception(result)


class HomeHandler(BaseHandler):

    async def get(self):
        """
        @author: SAM
        @CreateTime: 2021/6/10 16:42
        @UpdateTime(upf): 2021/6/10 16:42
        @desc: ''
        """
        # self.ValidateForm(MainTestForm)
        obj = MainTestForm()
        flag, success, error = obj.check_valid(self)
        result = {'flag': flag, 'success': success, 'error': error}
        if not flag:
            return self.write({'result': result})
        self.write({'result': result})


def make_app():
    return tornado.web.Application([
        (r"/", HomeHandler),
    ])


# endregion


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
