# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: AbstractFactoryPattern
# CreateTime: 2021/5/29 14:51
# Summary: '抽象工厂模式'


"""
AbstractFactoryPattern
抽象工厂模式
    特点：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类
"""


class IUser:

    def GetUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:00
        @updateTime(upf): 2021/5/29 15:00
        """
        ...

    def InsertUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:00
        @updateTime(upf): 2021/5/29 15:00
        """
        ...


class IDepartment:

    def GetDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:00
        @updateTime(upf): 2021/5/29 15:00
        """
        ...

    def InsertDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:01
        @updateTime(upf): 2021/5/29 15:01
        """
        ...


class CAccessUser(IUser):

    def GetUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:01
        @updateTime(upf): 2021/5/29 15:01
        """
        print('Access GetUser')

    def InsertUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:01
        @updateTime(upf): 2021/5/29 15:01
        """
        print('Access InsertUser')


class CAccessDepartment(IDepartment):

    def GetDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:02
        @updateTime(upf): 2021/5/29 15:02
        """
        print('Access GetDepartment')

    def InsertDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:03
        @updateTime(upf): 2021/5/29 15:03
        """
        print('Access InsertDepartment')


class CSqlUser(IUser):

    def GetUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:03
        @updateTime(upf): 2021/5/29 15:03
        """
        print('Sql GetUser')

    def InsertUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:04
        @updateTime(upf): 2021/5/29 15:04
        """
        print('Sql InsertUser')


class CSqlDepartment(IDepartment):

    def GetDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:07
        @updateTime(upf): 2021/5/29 15:07
        """
        print('Sql GetDepartment')

    def InsertDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:07
        @updateTime(upf): 2021/5/29 15:07
        """
        print('Sql InsertDepartment')


class IFactory:

    def CreateUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:08
        @updateTime(upf): 2021/5/29 15:08
        """
        ...

    def CreateDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:08
        @updateTime(upf): 2021/5/29 15:08
        """
        ...


class AccessFactory(IFactory):

    def CreateUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:09
        @updateTime(upf): 2021/5/29 15:09
        """
        temp = CAccessUser()
        return temp

    def CreateDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:09
        @updateTime(upf): 2021/5/29 15:09
        """
        temp = CAccessDepartment()
        return temp


class SqlFactory(IFactory):

    def CreateUser(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:10
        @updateTime(upf): 2021/5/29 15:10
        """
        temp = CSqlUser()
        return temp

    def CreateDepartment(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 15:10
        @updateTime(upf): 2021/5/29 15:10
        """
        temp = CSqlDepartment()
        return temp


if __name__ == '__main__':
    factory = SqlFactory()
    user = factory.CreateUser()
    depart = factory.CreateDepartment()
    user.GetUser()
    depart.GetDepartment()
