# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Decorate
# CreateTime: 2021/4/29 20:36
# Summary: ''


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
        # if not res or ('code' not in res.keys() and 'message' not in res.keys()) \
        #         or ('error_code' not in res.keys() and 'error_message' not in res.keys()):
        #     res = ReturnJson.SUCCESS()

        if res and 'code' in res.keys():
            ...
        elif res and 'error_code' in res.keys():
            ...
        else:
            res = ReturnJson.SUCCESS()

        # if res and 'code' not in res.keys():  # and 'message' not in res.keys()
        #     res = ReturnJson.SUCCESS()
        # elif res and 'error_code' not in res.keys():  # and 'error_message' not in res.keys()
        #     res = ReturnJson.SUCCESS()
        # else:  # 无内容，初始化
        #     res = ReturnJson.SUCCESS()

        self.json(res)

    return wrapper
