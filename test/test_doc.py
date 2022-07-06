# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: test_doc
# CreateTime: 2022/5/30 16:37
# Summary: ''

"""
@func name: 测试 获取方法注解
@desc:
    1.注解必须以""或'';
    2.此处优先级 < 类 < __init__ < 方法;
    3.格式：
        @author: 王康
        @email: 邮箱
@author: 土人土
@email: SAM-Turentu@outlook.com
@createTime: 2022/5/30 16:38
@updateTime(upf): 2022/5/30 16:38
"""

from functools import wraps


def get_doc(func):
    """
    获取 方法注释 __doc__
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        doc = func.__doc__
        email = doc.split('@')
        print(doc)

    return wrapper


class Home(object):
    """
    @author: 土人土 Home Class
    @email: SAM-Turentu@outlook.com
    """

    def __init__(self):
        ...

    @get_doc
    def get(self):
        """
        @func name: 获取返回数据
        @desc:
        @author: SAM(Home.get())
        @email: ainiruoxia@outlook.com
        @createTime: 2022/5/30 16:38
        @updateTime(upf): 2022/5/30 16:38
        """
        data = {'name': 'SAM', 'email': 'ainiruoxia@outlook.com'}
        print('get data: ', data)
        return data


def main():
    """
    @func name:
    @desc:
    @author: SAM(main func)
    @createTime: 2022/5/30 16:39
    @updateTime(upf): 2022/5/30 16:39
    """
    home = Home()
    data = home.get()
    ret = {'msg': 'success', 'status': True, 'data': data}
    return ret


if __name__ == '__main__':
    main()
