# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: SimpleFactoryPattern
# CreateTime: 2021/5/18 20:24
# Summary: '简单工厂模式'
# href https://www.cnblogs.com/wuyuegb2312/archive/2013/04/09/3008320.html


"""
SimpleFactoryPattern
简单工厂模式
    特点：工厂根据条件产生不同功能的类
"""


class Operation:
    def GetResult(self):
        pass


class OperationAdd(Operation):
    def GetResult(self):
        return self.op1 + self.op2


class OperationSub(Operation):
    def GetResult(self):
        return self.op1 - self.op2


class OperationMul(Operation):
    def GetResult(self):
        return self.op1 * self.op2


class OperationDiv(Operation):
    def GetResult(self):
        try:
            result = self.op1 / self.op2
            return result
        except:
            print("error:divided by zero.")
            return 0


class OperationUndef(Operation):
    def GetResult(self):
        print("Undefine operation.")
        return 0


class OperationFactory:
    operation = {}
    operation["+"] = OperationAdd()
    operation["-"] = OperationSub()
    operation["*"] = OperationMul()
    operation["/"] = OperationDiv()

    def createOperation(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op


if __name__ == "__main__":
    op = input("operator: ")
    opa = int(input("a: "))
    opb = int(input("b: "))
    factory = OperationFactory()
    cal = factory.createOperation(op)
    cal.op1 = opa
    cal.op2 = opb
    print(cal.GetResult())
