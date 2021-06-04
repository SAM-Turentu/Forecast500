# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseReturn
# CreateTime: 2021/6/4 9:51
# Summary: ''


class BaseReturn:

    def __call__(self, *args, **kwargs):
        """
        @author: SAM
        @CreateTime: 2021/6/4 11:17
        @UpdateTime(upf): 2021/6/4 11:17
        @desc: ''
        """
        return {**kwargs}


class Success(BaseReturn):

    def __call__(self, code=200, message='success', data=None):
        """
        @author: SAM
        @CreateTime: 2021/6/4 11:14
        @UpdateTime(upf): 2021/6/4 11:14
        @desc: ''
        """
        return {
            'code': code,
            'message': message,
            'data': data
        }


class NotFind(BaseReturn):

    def __call__(self, code=204, message='not find', data=None):
        """
        @author: SAM
        @CreateTime: 2021/6/4 11:14
        @UpdateTime(upf): 2021/6/4 11:14
        @desc: ''
        """
        return {
            'code': code,
            'message': message,
            'data': data
        }


class Failure(BaseReturn):

    def __call__(self, error_code=500, error_message='failure'):
        """
        @author: SAM
        @CreateTime: 2021/6/4 11:14
        @UpdateTime(upf): 2021/6/4 11:14
        @desc: ''
        """
        return {
            'error_code': error_code,
            'error_message': error_message,
        }


class SysException(BaseReturn):

    def __call__(self, error_code=500, error_message='failure'):
        """
        @author: SAM
        @CreateTime: 2021/6/4 14:32
        @UpdateTime(upf): 2021/6/4 14:32
        @desc: ''
        """
        return {
            'error_code': error_code,
            'error_message': error_message,
        }


class BaseReturnFactory:

    def ret_response(self):
        """
        @author: SAM
        @CreateTime: 2021/6/4 13:27
        @UpdateTime(upf): 2021/6/4 13:27
        @desc: ''
        """
        ...


class SuccessReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @author: SAM
        @CreateTime: 2021/6/4 13:27
        @UpdateTime(upf): 2021/6/4 13:27
        @desc: ''
        """
        return Success()


class FailureReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @author: SAM
        @CreateTime: 2021/6/4 13:55
        @UpdateTime(upf): 2021/6/4 13:55
        @desc: ''
        """
        return Failure()


class NotFindReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @author: SAM
        @CreateTime: 2021/6/4 14:33
        @UpdateTime(upf): 2021/6/4 14:33
        @desc: ''
        """
        return NotFind()


class SysExceptionReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @author: SAM
        @CreateTime: 2021/6/4 14:31
        @UpdateTime(upf): 2021/6/4 14:31
        @desc: ''
        """
        return SysException()


class ReturnJson:
    _success_ret = SuccessReturnFactory()
    SUCCESS = _success_ret.ret_response()

    _not_find_ret = NotFindReturnFactory()
    NOTFIND = _not_find_ret.ret_response()

    _failure_ret = FailureReturnFactory()
    FAILURE = _failure_ret.ret_response()

    _exception_ret = FailureReturnFactory()
    EXCEPTION = _exception_ret.ret_response()

# if __name__ == '__main__':
#     print(ReturnJson.SUCCESS(data={'name': 'Turnetu'}))
#     print(ReturnJson.NOTFIND(message='没有找到'))
#     print(ReturnJson.FAILURE(error_message='请求失败'))
#     print(ReturnJson.EXCEPTION(error_message='发生错误'))
