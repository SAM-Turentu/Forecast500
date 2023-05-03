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


# import sys
# if __name__ == '__main__':
#     res = ReturnJson(code=100, message='Hello，楠楠!')
#     aaa = ReturnJson.success()
#     bbb = aaa.__module__
#     # print(sys._getframe().f_code.co_name)
#     print(bbb)
#     hasattr(ReturnJson, bbb)
#     if isinstance(bbb, Result):
#         print(111)
#     else:
#         print(222)
#     print(ReturnJson.success(message='Hello World!'))
#     print(ReturnJson.notFind(message='Hello World! Not Find', code=404))


# class IReturn:
#
#     def __init__(self, code=None, message=None, data=None, error_code=None, error_message=None):
#         """
#         @author: SAM
#         @CreateTime: 2021/6/3 16:43
#         @UpdateTime(upf): 2021/6/3 16:43
#         @desc: ''
#         """
#         self.code = code
#         self.message = message
#         self.data = data
#         self.error_code = error_code
#         self.error_message = error_message
#
#     def GetReturn(self):
#         """
#         @author: SAM
#         @CreateTime: 2021/6/3 17:03
#         @UpdateTime(upf): 2021/6/3 17:03
#         @desc: ''
#         """
#         # return {
#         #     'code': self.code,
#         #     'message': self.message,
#         #     'data': self.data,
#         # }
#         ...
#
#     def GetErrorReturn(self):
#         """
#         @author: SAM
#         @CreateTime: 2021/6/3 17:04
#         @UpdateTime(upf): 2021/6/3 17:04
#         @desc: ''
#         """
#         # return {
#         #     'error_code': self.error_code,
#         #     'error_message': self.error_message,
#         # }
#         ...


# class Return(IReturn):
#
#     def GetReturn(self):
#         """
#         @author: SAM
#         @CreateTime: 2021/6/3 17:11
#         @UpdateTime(upf): 2021/6/3 17:11
#         @desc: ''
#         """
#         return {
#             'code': self.code,
#             'message': self.message,
#             'data': self.data,
#         }


class RetResponse:

    def ret_response(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/3 19:39
        @updateTime(upf): 2021/6/3 19:39
        """
        ...


class Success(RetResponse):

    def ret_response(self, code=None, message=None, data=None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/3 19:37
        @updateTime(upf): 2021/6/3 19:37
        """
        # self.code = code if code else 200
        # self.message = message if message else 'success'
        # self.data = data
        return {
            'code': code if code else 200,
            'message': message if message else 'success',
            'data': data,
        }


class NotFind(RetResponse):

    def ret_response(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/3 19:38
        @updateTime(upf): 2021/6/3 19:38
        """
        self.code = 204
        self.message = 'not find'
        self.data = None


class Failure(RetResponse):

    def ret_response(self, error_code=500, error_message='exception'):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/3 19:39
        @updateTime(upf): 2021/6/3 19:39
        """
        # self.error_code = 500
        # self.error_message = 'exception'
        return {
            'error_code': error_code,
            'error_message': error_message,
        }


class Return:
    def __init__(self, temp):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/3 19:53
        @updateTime(upf): 2021/6/3 19:53
        """
        self.temp = temp

    def __call__(self, code=200, message='', data=None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/3 20:21
        @updateTime(upf): 2021/6/3 20:21
        """
        return {
            'code': code,
            'message': message,
            'data': data,
        }

    def GetReturn(self, code=None, message=None, data=None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/3 19:54
        @updateTime(upf): 2021/6/3 19:54
        """
        a = self.temp.ret_response(code=code)
        return a


# ret = Return(Success())
# ret2 = Return(NotFind())
# ret3 = Return(Failure())
# print(ret.GetReturn(200))
# print(ret2.GetReturn(204))
# print(ret3.GetReturn(500))

if __name__ == '__main__':
    ret = Return(Success())
    ret2 = Return(NotFind())
    ret3 = Return(Failure())
    print(ret)
    a = ret3.GetReturn()
    print(a)
