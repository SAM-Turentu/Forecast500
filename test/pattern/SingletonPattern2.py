# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: SingletonPattern
# CreateTime: 2021/6/2 16:26
# Summary: '单例模式'


"""
SingletonPattern
单例模式
    特点：保证类仅有一个实例，并提供一个访问它的全局访问点
"""


# # 方法一：实现 __new__ 方法
# # 并在将一个类的实例绑定到类变量 _instance 上，
# class Singleton(object):
#
#     def __new__(cls, *args, **kwargs):
#         """
#         @author: SAM
#         @CreateTime: 2021/6/2 16:27
#         @UpdateTime(upf): 2021/6/2 16:27
#         @desc: ''
#         """
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class MyClass(Singleton):
#     a = 1
#
#
# one = MyClass()
# two = MyClass()
#
# two.a = 3
# print(one.a)
# print(id(one))
# print(id(two))
# print(one == two)
# print(one is two)


# # 方法二：共享属性（所谓单例就是所有引用（实例、对象）拥有相同的状态（属性）和行为（方法））
# # 同一个类的所有实例天然拥有相同的行为（方法）
# # 只需要保证同一个类的所有实例具有相同的状态（属性）即可
# # 所有实例共享属性的最简单最直接的方法就是 __dict__ 属性指向（引用）同一个字典（dict）
# class Borg(object):
#     _state = {}
#
#     def __new__(cls, *args, **kwargs):
#         """
#         @author: SAM
#         @CreateTime: 2021/6/2 16:34
#         @UpdateTime(upf): 2021/6/2 16:34
#         @desc: ''
#         """
#         ob = super(Borg, cls).__new__(cls, *args, **kwargs)
#         ob.__dict__ = cls._state
#         return ob
#
#
# class MyClass2(Borg):
#     a = 1
#
#
# one = MyClass2()
# two = MyClass2()
#
# two.a = 3
# print(one.a)
# print(id(one))
# print(id(two))
# print(one == two)
# print(one is two)


class Singleton2(type):

    def __init__(cls, name, bases, dict):
        """
        @author: SAM
        @CreateTime: 2021/6/2 17:22
        @UpdateTime(upf): 2021/6/2 17:22
        @desc: ''
        """
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        """
        @author: SAM
        @CreateTime: 2021/6/2 17:22
        @UpdateTime(upf): 2021/6/2 17:22
        @desc: ''
        """
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass3(object):
    __metaclass__ = Singleton2


one = MyClass3()
two = MyClass3()

two.a = 3
# print(one.a)
print(id(one))
print(id(two))
print(one == two)
print(one is two)
