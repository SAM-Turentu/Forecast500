# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: FormTest
# CreateTime: 2021/6/10 13:19
# Summary: ''


import re
from functools import wraps
from typing import Any
import tornado.web
import tornado.ioloop


def FromReturn(func):
    """
    @Author: SAM
    @CreateTime: 2021/6/24 10:29
    @UpdateTime(upf): 2021/6/24 10:29
    @Desc: ''
    """

    @wraps(func)
    def from_return(*args, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/24 10:31
        @UpdateTime(upf): 2021/6/24 10:31
        @Desc: ''
        """
        a = kwargs
        print(func)
        print(*args, **kwargs)
        return func(*args, **kwargs)

    return from_return


def from_return_test(form, vo=None):
    """
    @Author: SAM
    @CreateTime: 2021/6/24 10:37
    @UpdateTime(upf): 2021/6/24 10:37
    @Desc: ''
    """

    def fromreturn(func):
        """
        @Author: SAM
        @CreateTime: 2021/6/24 10:38
        @UpdateTime(upf): 2021/6/24 10:38
        @Desc: ''
        """

        @wraps(func)
        def from_return(handler):  # *args, **kwargs
            """
            @Author: SAM
            @CreateTime: 2021/6/24 10:38
            @UpdateTime(upf): 2021/6/24 10:38
            @Desc: ''
            """
            # obj = RegisterForm()
            flag, success, error = form.check_valid(handler)  # , vo
            result = {'flag': flag, 'success': success, 'error': error}
            if not flag:
                return handler.write({'result': result})
            handler.write({'result': result})
            return func(handler)  # func(*args, **kwargs)

        return from_return

    return fromreturn


class FieldName:
    label = None
    en_name = None


class BaseForm:

    def __init__(self, label: str = None, message=None, validators: list = None):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:19
        @UpdateTime(upf): 2021/6/10 13:19
        @desc: ''
        """
        self.value = None
        self.field_name = FieldName()
        self.field_name.label = label if label else self.field_name.en_name
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

        if not self.value and self.value != 0:
            self.success.update({
                self.field_name.en_name: self.value
            })
            return

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
        @Author: SAM
        @CreateTime: 2021/6/10 13:20
        @UpdateTime(upf): 2021/6/10 13:20
        @Desc: ''
        """
        self.value = value
        self.call_validators()  # 先执行附加条件，flag = False 不在继续执行下面方法
        # if not self.flag:
        #     return self

        pattern = '^.*$'
        self.match_input(pattern)

        return self


# region Description
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


class Files(BaseForm):

    def check_validate(self, value=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/21 16:48
        @UpdateTime(upf): 2021/6/21 16:48
        @Desc: ''
        """
        self.value = value
        self.call_validators()
        if not self.flag:
            return self
        pattern = ''
        self.match_input(pattern)
        return self


class DateRequired:

    def __init__(self, message=None):
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
        return cls  # type: BaseForm


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
                cls.error[cls.field_name.en_name] = [message]
        return cls


# todo 未写完
class NumofFile:

    def __init__(self, max_files=1, min_files=1, message=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/21 16:51
        @UpdateTime(upf): 2021/6/21 16:51
        @Desc: '文件数量'
        """
        self.min_files = min_files  # 文件最小数
        self.max_files = max_files  # 文件最大数
        self.message = message

    def __call__(self, cls):
        """
        @Author: SAM
        @CreateTime: 2021/6/21 16:52
        @UpdateTime(upf): 2021/6/21 16:52
        @Desc: ''
        """
        if not cls.value:
            cls.flag = False
            message = self.message if self.message else f'缺少{cls.field_name.label}'  # 缺少文件
        else:
            if len(cls.value) > self.max_files:
                message = self.message if self.message else f'{cls.field_name.label} 不能超过{self.max_files}个'  # 超过最大文件数
            else:
                ...

        return cls


# todo 未写完
class FileContentLength:

    def __init__(self, min_len=-1, max_len=-1, message=None):
        """
        @Author: SAM
        @CreateTime: 2021/6/21 16:59
        @UpdateTime(upf): 2021/6/21 16:59
        @Desc: '文件大小'
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
        @CreateTime: 2021/6/21 17:06
        @UpdateTime(upf): 2021/6/21 17:06
        @Desc: ''
        """
        if not cls.value:
            ...
        return cls


# endregion


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

        for key, forms in self.__dict__.items():
            forms.field_name.en_name = key

            if type(forms) is String:
                value = handler.get_query_argument(key, None)  # get
                # value = handler.get_argument(key, None)  # post
            elif type(forms) is Files:
                value = handler.request.files.get(key, None)
            # elif type(forms) is ValueList: # 多值：复选框
            #     value = handler.get_arguments(key, None)
            else:
                value = handler.get_argument(key, None)  # post

            # 此处调用校验器
            result = forms.check_validate(value=value)
            if result.flag:
                success_dict[key] = result.success[key]
            else:
                flag = False
                error_dict[key] = result.error[key]

        return flag, success_dict, error_dict


class RegisterForm(MainForm):

    def __init__(self):
        """
        @author: SAM
        @CreateTime: 2021/6/10 16:57
        @UpdateTime(upf): 2021/6/10 16:57
        @desc: ''
        """
        self.name = String(label='姓名', validators=[DateRequired('姓名为必填字段'), Length(2, 10, '姓名长度为2-10位')])
        self.age = String(label='年龄', validators=[DateRequired('年龄为必填字段'), Length(1, 3, '年龄长度为1-3位数字')])
        self.sex = String(label='性别')


# region Description
class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/15 12:51
        @UpdateTime(upf): 2021/6/15 12:51
        @Desc: ''
        """
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        """
        @Author: SAM
        @CreateTime: 2021/6/16 11:06
        @UpdateTime(upf): 2021/6/16 11:06
        @Desc: ''
        """
        exc_cls, exc_instance, trace = kwargs.get('exc_info')
        if status_code != 200:
            self.set_status(status_code)
            self.write(exc_instance.__str__())

    def ValidateForm(self, form):
        """
        @Author: SAM
        @CreateTime: 2021/6/15 12:53
        @UpdateTime(upf): 2021/6/15 12:53
        @Desc: ''
        """
        if callable(form):
            obj = form()
            flag, success, error = obj.check_valid(self)
            result = {'flag': flag, 'success': success, 'error': error}
            if not flag:
                self.write({'result': result})
                # raise Exception(result)


class HomeHandler(BaseHandler):

    # @FromReturn
    @from_return_test(RegisterForm())
    async def get(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/10 16:42
        @UpdateTime(upf): 2021/6/10 16:42
        @Desc: ''
        """
        print('已经执行!')
        # self.ValidateForm(MainTestForm)
        # obj = RegisterForm()
        # flag, success, error = obj.check_valid(self)
        # result = {'flag': flag, 'success': success, 'error': error}
        # if not flag:
        #     return self.write({'result': result})
        # self.write({'result': result})


def make_app():
    return tornado.web.Application([
        (r"/", HomeHandler),
    ])


# endregion


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
