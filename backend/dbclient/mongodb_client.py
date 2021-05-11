# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: mongodb_client
# CreateTime: 2021/4/27 21:49
# Summary: ''


import motor.motor_tornado


class MongoDBClient(object):
    _instance = None

    @classmethod
    def getInstance(cls, host='localhost', port=27017, user=None, password=None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/4/29 20:48
        @updateTime(upf): 2021/4/29 20:48
        """
        if cls._instance is None:
            cls._instance = cls(host, port, user, password)
        return cls._instance

    def __init__(self, host='localhost', port=27017, user=None, password=None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/4/27 21:38
        @updateTime(upf): 2021/4/27 21:38
        """
        self.client = motor.motor_tornado.MotorClient(host, port)
        self.database = self.client.Forecast500
        self.collection = self.database.BallData
        # self.BallData = self.database.BallData

    # async def SAM_Insert_Test(self):
    #     """
    #     @func name:
    #     @desc:
    #     @author: SAM
    #     @createTime: 2021/4/27 21:39
    #     @updateTime(upf): 2021/4/27 21:39
    #     """
    #     try:
    #         data = {'key': 'value'}
    #         result = await self.collection.insert(data)
    #     except Exception as e:
    #         print(e)
