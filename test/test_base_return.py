# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: test_base_return
# CreateTime: 2021/10/14 19:53
# Summary: ''


from functools import wraps, lru_cache
from timeit import Timer


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

    # def remove_mongodb_object_id(self):
    #     """
    #     删除 MongoDB 中的 _id
    #     data_source: False: 非mongodb，True：数据来自mongodb 必须删除 _id
    #     """
    #     data_type = type(self.data)
    #
    #     def _func(data):
    #         """
    #         递归方法
    #         todo 待优化
    #         """
    #         if type(data) == dict:
    #             if '_id' in data.keys():
    #                 del data['_id']
    #             # 字典的键中包含 list 类型数据
    #             for k, v in data.items():
    #                 if type(v) == list:
    #                     return _func(v)
    #
    #         if type(data) == list:
    #             for item in data:
    #                 return _func(item)
    #
    #     if data_type == list:
    #         for item in self.data:
    #             return _func(item)  # 调用递归方法
    #
    #     if data_type == dict:
    #         if '_id' in self.data.keys():
    #             del self.data['_id']
    #         for k, v in self.data.items():
    #             if type(v) == list:
    #                 return _func(v)  # 调用递归方法

    # @lru_cache(maxsize=None)
    # def remove_mongodb_object_id(self, data):
    #     """
    #     @func name:
    #     @desc:
    #     @author: SAM
    #     @createTime: 2021/10/18 21:14
    #     @updateTime(upf): 2021/10/18 21:14
    #     """
    #     try:
    #         print(data)
    #         data_type = type(data)
    #         # data_type = list
    #         if data_type == dict:
    #             # todo 删除操作并遍历判断是否有list
    #             if '_id' in data.keys():
    #                 del data['_id']
    #             for k, v in data.items():
    #                 if type(v) == list:
    #                     return self.remove_mongodb_object_id(v)
    #             return data
    #         if data_type == list:
    #             for item in data:
    #                 return self.remove_mongodb_object_id(item)
    #     except Exception as e:
    #         print(e)


class Success():

    # def __call__(self, code=200, message='success', data=None, **kwargs):
    #     """
    #     @Author: SAM
    #     @CreateTime: 2021/6/4 11:14
    #     @UpdateTime(upf): 2021/6/4 11:14
    #     @Desc: '请求成功，并正确响应'
    #     """
    #     self.data = data
    #     print(type(self.data))
    #     if kwargs.get('from_mongdb') and data:  # 正确返回数据时，才会可能删除 MongoDB 中的 _id，其他类中不需要调用该方法
    #         self.remove_mongodb_object_id(data)
    #     _ret = {
    #         'code': code,
    #         'message': message,
    #         'data': data,
    #         **kwargs
    #     }
    #     return _ret

    def remove_data(self, code=200, message='success', data=None, **kwargs):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/10/21 21:00
        @updateTime(upf): 2021/10/21 21:00
        """
        self.data = data
        if kwargs.get('from_mongdb') and data:  # 正确返回数据时，才会可能删除 MongoDB 中的 _id，其他类中不需要调用该方法
            self.remove_mongodb_object_id(data)
        _ret = {
            'code': code,
            'message': message,
            'data': data,
            **kwargs
        }
        return _ret

    # @lru_cache(maxsize=None)
    def remove_mongodb_object_id(self, data):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/10/18 21:14
        @updateTime(upf): 2021/10/18 21:14
        """
        try:
            # data = self.data
            # data_type = type(data)
            if type(data) == dict:
                # todo 删除操作并遍历判断是否有list
                if '_id' in data.keys():
                    del data['_id']
                for k, v in data.items():
                    if type(v) == list:
                        return self.remove_mongodb_object_id(v)
                return data
            if type(data) == list:
                for item in data:
                    return self.remove_mongodb_object_id(item)
        except Exception as e:
            print(e)


class BaseReturnFactory:

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 13:27
        @UpdateTime(upf): 2021/6/4 13:27
        @Desc: ''
        """
        ...


class SuccessReturnFactory(BaseReturnFactory):

    def ret_response(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/4 13:27
        @UpdateTime(upf): 2021/6/4 13:27
        @Desc: ''
        """
        return Success()


# class ReturnJson:
#     _success_ret = SuccessReturnFactory()
#     SUCCESS = _success_ret.ret_response()


@lru_cache(maxsize=None)  # maxsize 为 None 时，缓存可以不受限制地增长
def fib_cache(n):
    """
    @func name:
    @desc:
    @author: SAM
    @createTime: 2021/10/18 19:22
    @updateTime(upf): 2021/10/18 19:22
    """
    if n <= 2:
        return 1
    else:
        print('n: ', n)
        return fib_cache(n - 1) + fib_cache(n - 2)


if __name__ == '__main__':
    print(fib_cache(10))

# if __name__ == '__main__':
#     data = {
#         'name': 'SAM',
#         'age': 27,
#         '_id': 'asdf412153e1rvaszdf',
#
#     }
#     _data = [
#         {
#             'name': 'SAM',
#             'age': 27,
#             '_id': 'asdf412153e1rvaszdf1234',
#             'subjects': [
#                 {
#                     '_id': '1234asdf412153e1rvaszdf',
#                     'name': '语文',
#                     'teacher': '孙自平',
#                     'scores': [80, 77, 83],
#                 }, {
#                     '_id': '123asdf412153e1rvaszdf',
#                     'name': '数学',
#                     'teacher': '赵金龙',
#                     'scores': [112, 128, 124, 120],
#                 },
#             ]
#         },
#         {
#             'name': 'Turentu',
#             'age': 27,
#             '_id': 'asdf412153e1rvaszdf123',
#             'subjects': [{
#                 '_id': '123asdf412153e1rvaszdf',
#                 'name': '数学',
#                 'teacher': '赵金龙',
#                 'scores': [98, 102, 110, 135],
#             },
#             ]
#         }
#     ]
#     a = Success()
#     ret = a.remove_data(code=200, message='请求成功!', data=_data, from_mongdb=True)
#     # ret = a(code=200, message='请求成功!', data=data, from_mongdb=True)
#     print(f'ret ({type(ret["data"])}) = {ret}')
    # ReturnJson.SUCCESS(code=200, message='请求成功!', data=data, from_mongdb=True)
    # ret = ReturnJson.SUCCESS(
    #     data=[
    #         {
    #             'name': 'SAM',
    #             'age': 27,
    #             'subjects': [
    #                 {
    #                     'name': '语文',
    #                     'teacher': '孙自平',
    #                     'scores': [80, 77, 83],
    #                 }, {
    #                     'name': '数学',
    #                     'teacher': '赵金龙',
    #                     'scores': [112, 128, 124, 120],
    #                 },
    #             ]
    #         },
    #         {
    #             'name': 'Turentu',
    #             'age': 27,
    #             'subjects': [
    #                 {
    #                     'name': '语文',
    #                     'teacher': '孙自平',
    #                     'scores': [120, 99, 115],
    #                 }, {
    #                     'name': '数学',
    #                     'teacher': '赵金龙',
    #                     'scores': [98, 102, 110, 135],
    #                 },
    #             ]
    #         }
    #     ],
    #     message='请求成功!', code=200, from_mongdb=True)
    # print(ret)
