# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Result
# CreateTime: 2021/4/30 21:30
# Summary: ''


# todo 添加一个类 定义code值
class BaseReturn(object):
    __slots__ = ('code', 'message', 'data')

    def __init__(self, code: int = 200, message: str = '', data=None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/4/30 22:02
        @updateTime(upf): 2021/4/30 22:02
        """
        self.code = code
        self.message = message
        self.data = data

    def __call__(self, code=200, message='', data=None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/1 10:07
        @updateTime(upf): 2021/5/1 10:07
        """
        return {
            'code': code,
            'message': message,
            'data': data,
        }


class Result(object):

    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/1 10:08
        @updateTime(upf): 2021/5/1 10:08
        """
        self.return_json = BaseReturn()

    def __call__(self, code=200, message='success', data=None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/1 10:28
        @updateTime(upf): 2021/5/1 10:28
        """
        return self.return_json(code, message, data)

    def success(self, code=200, message='success', data=None):
        """
        @func name: 请求成功
        @desc:
        @author: SAM
        @createTime: 2021/4/30 23:06
        @updateTime(upf): 2021/4/30 23:06
        """
        return self.return_json(code, message, data)

    def notFind(self, code=201, message='not find'):
        """
        @func name:请求成功，但无资源返回
        @desc:
        @author: SAM
        @createTime: 2021/5/1 10:17
        @updateTime(upf): 2021/5/1 10:17
        """
        return self.return_json(code, message)

    def exception(self, code=500, message='系统内部错误'):
        """
        @func name:系统异常
        @desc:
        @author: SAM
        @createTime: 2021/5/1 10:20
        @updateTime(upf): 2021/5/1 10:20
        """
        return self.return_json(code, message)


ReturnJson = Result()
