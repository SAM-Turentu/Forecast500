# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: test_base_return
# CreateTime: 2021/10/14 19:53
# Summary: ''
from functools import wraps


# def fib_recur(n):
#     assert n >= 0, "n > 0"
#     if n <= 1:
#         return n
#     return fib_recur(n - 1) + fib_recur(n - 2)
#
#
# for i in range(1, 20):
#     print(fib_recur(i), end=' ')


class BaseReturn:

    def __call__(self, *args, **kwargs):
        """
        @author: SAM
        @CreateTime: 2021/6/4 11:17
        @UpdateTime(upf): 2021/6/4 11:17
        @desc: ''
        """
        print('kwargs: ', kwargs)
        return {**kwargs}

    def remove_mongodb_object_id(self):
        """
        删除 MongoDB 中的 _id
        data_source: False: 非mongodb，True：数据来自mongodb 必须删除 _id
        """
        data_type = type(self.data)

        def _func(data):
            """
            递归方法
            todo 待优化
            """
            if type(data) == dict:
                if '_id' in data.keys():
                    del data['_id']
                # 字典的键中包含 list 类型数据
                for k, v in data.items():
                    if type(v) == list:
                        return _func(v)

            if type(data) == list:
                for item in data:
                    return _func(item)

        if data_type == list:
            for item in self.data:
                return _func(item)  # 调用递归方法

        if data_type == dict:
            if '_id' in self.data.keys():
                del self.data['_id']
                for k, v in self.data.items():
                    if type(v) == list:
                        return _func(v)  # 调用递归方法


class Success(BaseReturn):

    def __call__(self, code=200, message='success', data=None, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 11:14
        @UpdateTime(upf): 2021/6/4 11:14
        @Desc: '请求成功，并正确响应'
        """
        self.data = data
        if kwargs.get('from_mongdb'):  # 正确返回数据时，才会可能删除 MongoDB 中的 _id，其他类中不需要调用该方法
            self.remove_mongodb_object_id()
        _ret = {
            'code': code,
            'message': message,
            'data': data,
            **kwargs
        }
        return _ret


class BaseReturnFactory:

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 13:27
        @UpdateTime(upf): 2021/6/4 13:27
        @Desc: ''
        """
        ...

    # todo 删除 MongoDB 中的 _id
    def _remove_mongodb_object_id(self, from_mongdb=False):
        """
        删除 MongoDB 中的 _id
        data_source: False: 非mongodb，True：数据来自mongodb 必须删除 _id
        """
        if from_mongdb:
            data_type = type(self.data)
            if data_type == list:
                for item in self.data:
                    del item['_id']
            if data_type == dict:
                del self.data['_id']


class SuccessReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 13:27
        @UpdateTime(upf): 2021/6/4 13:27
        @Desc: ''
        """
        return Success()


class ReturnJson:
    _success_ret = SuccessReturnFactory()
    SUCCESS = _success_ret.ret_response()


if __name__ == '__main__':
    ret = ReturnJson.SUCCESS(
        data=[{
            'name': 'SAM',
            'age': 27,
            'subjects': [
                {
                    'name': '语文',
                    'teacher': '孙自平',
                    'scores': [80, 77, 83],
                }, {
                    'name': '数学',
                    'teacher': '赵金龙',
                    'scores': [112, 128, 124, 120],
                },
            ]
        },
            {'name': 'SAM', 'age': 27}
        ],
        message='请求成功!', code=200, from_mongdb=True)
    print(ret)
