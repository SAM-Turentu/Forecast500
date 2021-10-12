# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: sorts
# CreateTime: 2021/8/18 20:52
# Summary: '排序方法'


import random
import time
from urllib import request, error
from functools import lru_cache


@lru_cache()  # 测试无缓存时将本行注释掉
def fib_memoization(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1

    return fib_memoization(number - 1) + fib_memoization(number - 2)


@lru_cache(1)
def sam_cache():
    """
    @func name:
    @desc:
    @author: SAM
    @createTime: 2021/9/5 10:26
    @updateTime(upf): 2021/9/5 10:26
    """
    return [random.randint(0, 20) for _ in range(10)]


@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'https://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with request.urlopen(resource) as s:
            return s.read()
    except error.HTTPError:
        return 'Not Found'


def main():
    """
    @func name:
    @desc:
    @author: SAM
    @createTime: 2021/9/5 10:24
    @updateTime(upf): 2021/9/5 10:24
    """
    try:
        for n in 8, 290, 308, 320, 8, 320:  # , 218, 320, 279, 289, 320, 9991
            pep = get_pep(n)
            print(n, len(pep))
        a = get_pep.cache_info()
        print(a)
        print('asdf')
        # data = sam_cache()
        # a = sam_cache.cache_info()
        # print(a)
        # print(a)
        # print(data)
    except Exception as e:
        print(e)


import pandas as pd
import pymongo
if __name__ == '__main__':
    client = pymongo.MongoClient(host='localhost', port=27017)
    my_db = client['forecast500']
    my_collection = my_db['union_lotto']
    data = pd.DataFrame(list(my_collection.find().limit(10)))
    print(data)
    main()
#
#
# start = time.time()
# res = fib_memoization(33)
# print(res)
# print(f'耗时: {time.time() - start}s')
#
