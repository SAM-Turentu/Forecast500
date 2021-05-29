# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: FactoryMethodPattern
# CreateTime: 2021/5/29 11:01
# Summary: '工厂方法模式'


"""
FactoryMethodPattern
工厂方法模式
    特点：定义一个用于创建对象的接口，让子类决定实例化哪一个类。这使得一个类的实例化延迟到其子类。
"""


class LeiFeng:

    def Sweep(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 14:37
        @updateTime(upf): 2021/5/29 14:37
        """
        print('LeiFeng sweep')


class Student(LeiFeng):

    def Sweep(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 14:40
        @updateTime(upf): 2021/5/29 14:40
        """
        print('Student sweep')


class Volenter(LeiFeng):

    def Sweep(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 14:40
        @updateTime(upf): 2021/5/29 14:40
        """
        print('Volenter sweep')


class LeiFengFactory:

    def CreateLeiFeng(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 14:41
        @updateTime(upf): 2021/5/29 14:41
        """
        temp = LeiFeng()
        return temp


class StudentFactory(LeiFengFactory):

    def CreateLeiFeng(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 14:42
        @updateTime(upf): 2021/5/29 14:42
        """
        temp = Student()
        return temp


class VolenterFactory(LeiFengFactory):

    def CreateLeiFeng(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 14:42
        @updateTime(upf): 2021/5/29 14:42
        """
        temp = Volenter()
        return temp


if __name__ == '__main__':
    sf = StudentFactory()
    s = sf.CreateLeiFeng()
    s.Sweep()
    sdf = VolenterFactory()
    sd = sdf.CreateLeiFeng()
    sd.Sweep()
