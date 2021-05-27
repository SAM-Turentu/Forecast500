# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: ProxyPattern
# CreateTime: 2021/5/18 21:18
# Summary: '代理模式'


class Interface:
    def Request(self):
        return 0


class RealSubject(Interface):
    def Request(self):
        print("Real request.")


class Proxy(Interface):
    def Request(self):
        self.real = RealSubject()
        self.real.Request()


if __name__ == "__main__":
    p = Proxy()
    p.Request()
