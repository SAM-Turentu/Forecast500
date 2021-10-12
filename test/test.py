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
import random
import time
from multiprocessing import Queue, Process


# region Multiprocessing
def consumer(q, name):
    """
    @Author: SAM
    @CreateTime: 2021/8/11 13:29
    @UpdateTime(upf): 2021/8/11 13:29
    @Desc: ''
    """
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print(f"\033[43m {name} 吃{res}\033[0m")


def producer(q, name, food, counts):
    """
    @Author: SAM
    @CreateTime: 2021/8/11 13:30
    @UpdateTime(upf): 2021/8/11 13:30
    @Desc: ''
    """
    for i in range(counts):
        time.sleep(random.randint(1, 3))
        res = f'{food} {i}'
        q.put(res)
        print(f"\033[45m {name} 生产了 {res}\033[0m")


# endregion

def bubbleSort(array: list):
    """
    @Author: SAM
    @CreateTime: 2021/8/18 14:55
    @UpdateTime(upf): 2021/8/18 14:55
    @Desc: ''
    """
    flag = True
    times = 0
    for i in range(len(array) - 1):
        if not flag: break
        flag = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                times += 1
                flag = True
    print(f'冒泡排序：array = {array}，执行了 {times} 次')


def selectionSort(array: list):
    """
    @Author: SAM
    @CreateTime: 2021/8/18 15:03
    @UpdateTime(upf): 2021/8/18 15:03
    @Desc: ''
    """
    times = 0
    for i in range(len(array) - 1):
        a = i
        for j in range(i + 1, len(array)):
            if array[j] < array[a]:
                a = j

        if a != i:
            array[i], array[a] = array[a], array[i]

    print(f'冒泡排序：array = {array}，执行了 {times} 次')


if __name__ == '__main__':
    array = [2, 5, 3, 65, 6, 7, 67, 4, 32, 48]
    bubbleSort(array)  # 冒泡排序
    selectionSort(array)  # 选择排序

    # q = Queue()
    # p1 = Process(target=producer, args=(q, 'egon', '包子', 3))
    # c1 = Process(target=consumer, args=(q, 'mike'))
    # p1.start()
    # c1.start()
    # print('main func')
