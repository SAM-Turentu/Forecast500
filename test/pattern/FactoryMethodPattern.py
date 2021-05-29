# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: FactoryMethodPattern
# CreateTime: 2021/5/26 13:10
# Summary: '工厂方法模式'

"""
模式特点：定义一个用于创建对象的接口，让子类决定实例化哪一个类。这使得一个类的实例化延迟到其子类。
"""


class LeiFeng:

    def Sweep(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:15
        @UpdateTime(upf): 2021/5/26 13:15
        @desc: ''
        """
        print('LeiFeng sweep')


class Student(LeiFeng):

    def Sweep(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:16
        @UpdateTime(upf): 2021/5/26 13:16
        @desc: ''
        """
        print('Student sweep')


class Volenter(LeiFeng):

    def Sweep(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:16
        @UpdateTime(upf): 2021/5/26 13:16
        @desc: ''
        """
        print('Volenter sweep')


class LeiFengFactory:

    def CreateLeiFeng(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:17
        @UpdateTime(upf): 2021/5/26 13:17
        @desc: ''
        """
        temp = LeiFeng()
        return temp


class StudentFactory(LeiFengFactory):

    def CreateLeiFeng(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:18
        @UpdateTime(upf): 2021/5/26 13:18
        @desc: ''
        """
        temp = Student()
        return temp


class VolenterFactory(LeiFengFactory):

    def CreateLeiFeng(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:18
        @UpdateTime(upf): 2021/5/26 13:18
        @desc: ''
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
