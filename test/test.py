# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: test
# CreateTime: 2021/6/18 9:58
# Summary: ''


class A:

    def __init__(self, func):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/8/4 20:40
        @updateTime(upf): 2021/8/4 20:40
        """
        print('定义初始化函数')
        print('func name is ', func.__name__)
        self.__func = func

    def __call__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/8/4 20:41
        @updateTime(upf): 2021/8/4 20:41
        """
        print('call 方法作为装饰器的功能')
        self.__func()
        print('增加的功能2')


@A
def B():
    """
    @func name:
    @desc:
    @author: SAM
    @createTime: 2021/8/4 20:43
    @updateTime(upf): 2021/8/4 20:43
    """
    print('这是B 是原函数')


if __name__ == '__main__':
    # A(B)
    B()
