# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseReturn
# CreateTime: 2021/6/4 9:51
# Summary: '响应统一化'

# todo code 需要调整

# region Description
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

    def __call__(self, code=200, message='success', data=None, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 11:14
        @UpdateTime(upf): 2021/6/4 11:14
        @Desc: '请求成功，并正确响应'
        """
        return {
            'code': code,
            'message': message,
            'data': data,
            **kwargs
        }


class NotFind(BaseReturn):

    def __call__(self, code=204, message='not find', data=None, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 11:14
        @UpdateTime(upf): 2021/6/4 11:14
        @Desc: '请求已处理，但无内容'
        """
        return {
            'code': code,
            'message': message,
            'data': data,
            **kwargs
        }


class InvalidParams(BaseReturn):

    def __call__(self, error_code=400, error_message='invalid parameter', error_details: dict = {}, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/24 12:48
        @UpdateTime(upf): 2021/6/24 12:48
        @Desc: '无效参数'
        """
        return {
            'error_code': error_code,
            'error_message': error_message,
            'error_details': error_details,
            **kwargs
        }


class Failure(BaseReturn):

    def __call__(self, error_code=500, error_message='failure', **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 11:14
        @UpdateTime(upf): 2021/6/4 11:14
        @Desc: '请求失败'
        """
        return {
            'error_code': error_code,
            'error_message': error_message,
            **kwargs
        }


class HandlerException(BaseReturn):

    def __call__(self, *args, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/30 13:23
        @UpdateTime(upf): 2021/6/30 13:23
        @Desc: 'BaseHandler write_error 独享'
        """
        if 'error_code' not in kwargs:
            kwargs['error_code'] = 500
        return {**kwargs}


class BASEEXCEPTION(Exception):
    ...


class SysException(BASEEXCEPTION):

    def __init__(self, error_code=500, error_message='system exception!'):
        """
        @Author: SAM
        @CreateTime: 2021/6/30 11:02
        @UpdateTime(upf): 2021/6/30 11:02
        @Desc: ''
        """
        self.error_code = error_code
        self.error_message = error_message
        Exception.__init__(self, self.error_code, self.error_message)

    # def __call__(self, error_code=500, error_message='failure'):
    #     """
    #     @Author: SAM
    #     @CreateTime: 2021/6/4 14:32
    #     @UpdateTime(upf): 2021/6/4 14:32
    #     @Desc: '请求内部异常'
    #     """
    #     return {
    #         'error_code': error_code,
    #         'error_message': error_message,
    #     }


class BaseReturnFactory:

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 13:27
        @UpdateTime(upf): 2021/6/4 13:27
        @Desc: ''
        """
        ...


class SuccessReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 13:27
        @UpdateTime(upf): 2021/6/4 13:27
        @Desc: ''
        """
        return Success()


class InvalidParamsReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/24 13:15
        @UpdateTime(upf): 2021/6/24 13:15
        @Desc: ''
        """
        return InvalidParams()


class FailureReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 13:55
        @UpdateTime(upf): 2021/6/4 13:55
        @Desc: ''
        """
        return Failure()


class NotFindReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 14:33
        @UpdateTime(upf): 2021/6/4 14:33
        @Desc: ''
        """
        return NotFind()


class HandlerExceptionReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/30 13:24
        @UpdateTime(upf): 2021/6/30 13:24
        @Desc: 'BaseHandler write_error 独享'
        """
        return HandlerException()


class SysExceptionReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 14:31
        @UpdateTime(upf): 2021/6/4 14:31
        @Desc: ''
        """
        return SysException  # 不要加()，不在此处实例化


# endregion


class ReturnJson:
    _success_ret = SuccessReturnFactory()
    SUCCESS = _success_ret.ret_response()

    _invalid_params_ret = InvalidParamsReturnFactory()
    INVALIDPARAMS = _invalid_params_ret.ret_response()

    _not_find_ret = NotFindReturnFactory()
    NOTFIND = _not_find_ret.ret_response()

    _failure_ret = FailureReturnFactory()
    FAILURE = _failure_ret.ret_response()

    _exception_ret = SysExceptionReturnFactory()
    EXCEPTION = _exception_ret.ret_response()

    # region BaseHandler write_error 独享
    _Handler_Exception = HandlerExceptionReturnFactory()
    HANDLER_EXCEPTION = _Handler_Exception.ret_response()
    # endregion
