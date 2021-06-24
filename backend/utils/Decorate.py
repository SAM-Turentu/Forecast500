# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Decorate
# CreateTime: 2021/4/29 20:36
# Summary: '装饰器'


from functools import wraps
from backend.utils.BaseReturn import ReturnJson


def DI(**kwargs):
    """
    @func name: 注入装饰
    @desc:
    @author: SAM
    @createTime: 2021/4/29 20:37
    @updateTime(upf): 2021/4/29 20:37
    """

    def outer(cls):
        """
        @func name:
        @desc: 注入一个属性
        @author: SAM
        @createTime: 2021/4/29 20:37
        @updateTime(upf): 2021/4/29 20:37
        """
        for x in kwargs:
            setattr(cls, x, kwargs.get(x))
        return cls

    return outer


def Return(func):
    """
    @func name: 拦截方法返回，controller 层方法无需手动编写返回代码
    @desc:
    @author: SAM
    @createTime: 2021/4/30 21:28
    @updateTime(upf): 2021/4/30 21:28
    """

    async def wrapper(self, *args, **kwargs):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/5 16:42
        @updateTime(upf): 2021/5/5 16:42
        """
        res = await func(self, *args, **kwargs)
        if not res:
            res = ReturnJson.SUCCESS()
        self.json(res)

    return wrapper


# todo 重置form表单，待优化
def form_reset(form):
    """
    @Author: SAM
    @CreateTime: 2021/6/24 16:30
    @UpdateTime(upf): 2021/6/24 16:30
    @Desc: '重置'
    """
    for k, v in form.__dict__.items():
        v.error = {}
        v.flag = True
        v.success = {}
        v.values = None


def CheckFrom(form, vo):
    """
    @Author: SAM
    @CreateTime: 2021/6/24 10:53
    @UpdateTime(upf): 2021/6/24 10:53
    @Desc: ''
    """

    def FromReturn(func):
        """
        @Author: SAM
        @CreateTime: 2021/6/24 10:53
        @UpdateTime(upf): 2021/6/24 10:53
        @Desc: ''
        """

        @wraps(func)
        async def from_return(handler):
            """
            @Author: SAM
            @CreateTime: 2021/6/24 10:54
            @UpdateTime(upf): 2021/6/24 10:54
            @Desc: ''
            """
            form_reset(form)  # todo 重置form， 待优化
            flag, success, error = form.check_valid(handler, vo)
            if not flag:
                return ReturnJson.INVALIDPARAMS(error_message='请求参数错误!', error_details=error)
            # 将 result 存储
            handler.form = success

            return await func(handler)

        return from_return

    return FromReturn
