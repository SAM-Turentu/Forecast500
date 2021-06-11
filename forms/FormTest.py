# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: FormTest
# CreateTime: 2021/6/10 13:19
# Summary: ''


import tornado.web
import tornado.ioloop


class BaseForm:

    def __init__(self, label: str = None, validators: list = None):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:19
        @UpdateTime(upf): 2021/6/10 13:19
        @desc: ''
        """
        self.name_d = {'label': label, 'en_name': None}
        self.value = None
        self.handler = None
        self.flag = True
        self.success = {}
        self.error = {}
        self.validators = validators
        # self.call_validators()  # 初始化不调用

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
                    validator(self, self.name_d, self.value)
                else:
                    raise Exception('This func do not callable.')
                # callable(validator(self.name, self.value))


class String(BaseForm):

    def check_validate(self, en_name=None, value=None):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:20
        @UpdateTime(upf): 2021/6/10 13:20
        @desc: ''
        """
        # self.name_d['en_name'] = en_name
        self.value = value
        self.call_validators()

        self.STRING = '^.*$'
        self.TEXT = '^[\s\S]*$'

        # 使用正则表达式 验证

        return self


class Float(BaseForm):

    def check_validate(self, en_name=None, value=None):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:20
        @UpdateTime(upf): 2021/6/10 13:20
        @desc: ''
        """
        self.name_d['en_name'] = en_name
        self.value = value
        self.call_validators()


class DateRequired:

    def __init__(self, message):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:25
        @UpdateTime(upf): 2021/6/10 13:25
        @desc: ''
        """
        self.message = message

    def __call__(self, cls, name_d, value):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:27
        @UpdateTime(upf): 2021/6/10 13:27
        @desc: ''
        """
        if not value:
            cls.flag = False
            message = self.message if self.message else f'{name_d["label"]} 为必填项'
            cls.error[name_d['en_name']] = message
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

    def __call__(self, cls, name_d, value):
        """
        @author: SAM
        @CreateTime: 2021/6/10 13:28
        @UpdateTime(upf): 2021/6/10 13:28
        @desc: ''
        """
        if len(value) < self.min_len:
            cls.flag = False
            message = self.message if self.message else f'{name_d["label"]} 长度不足'
            cls.error[name_d['en_name']] = message
        if len(value) > self.max_len:
            cls.flag = False
            message = self.message if self.message else f'{name_d["label"]} 长度超出'
            cls.error[name_d['en_name']] = message
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
            validator.name_d['en_name'] = key
            if type(validator) is String:
                # 此处调用校验器
                result = validator.check_validate(en_name=key, value=value)

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


class HomeHandler(tornado.web.RequestHandler):

    async def get(self):
        """
        @author: SAM
        @CreateTime: 2021/6/10 16:42
        @UpdateTime(upf): 2021/6/10 16:42
        @desc: ''
        """
        obj = MainTestForm()
        flag, success, error = obj.check_valid(self)
        result = {'flag': flag, 'success': success, 'error': error}
        self.write({'result': result})


def make_app():
    return tornado.web.Application([
        (r"/", HomeHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
