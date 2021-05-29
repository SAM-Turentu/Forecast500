# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: PrototypePattern
# CreateTime: 2021/5/26 13:34
# Summary: '原型模式'


"""
PrototypePattern
原型模式
    特点：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象
"""

import copy


class WorkExp:
    place = ''
    year = 0


class Resume:
    name = ''
    age = 0

    def __init__(self, n):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:43
        @UpdateTime(upf): 2021/5/26 13:43
        @desc: ''
        """
        self.name = n

    def SetAge(self, a):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:43
        @UpdateTime(upf): 2021/5/26 13:43
        @desc: ''
        """
        self.age = a

    def SetWorkWxp(self, p, y):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:44
        @UpdateTime(upf): 2021/5/26 13:44
        @desc: ''
        """
        self.place = p
        self.year = y

    def Display(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:44
        @UpdateTime(upf): 2021/5/26 13:44
        @desc: ''
        """
        print(self.age)
        print(self.place)
        print(self.year)

    def Clone(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 13:44
        @UpdateTime(upf): 2021/5/26 13:44
        @desc: ''
        """
        return self


if __name__ == '__main__':
    a = Resume('a')
    b = a.Clone()
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a.SetAge(3)
    b.SetAge(4)
    c.SetAge(5)
    d.SetAge(6)
    a.SetWorkWxp('PrimarySchool', 1996)
    b.SetWorkWxp('MidSchool', 2001)
    c.SetWorkWxp('HighSchool', 2004)
    d.SetWorkWxp('University', 2007)
    a.Display()
    b.Display()
    c.Display()
    d.Display()
