# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: SoruceDataDAO
# CreateTime: 2021/4/29 20:23
# Summary: '原始数据处理 ==> mongodb'


from dao.BaseDAO import BaseDAO


class SourceDataDAO(BaseDAO):

    async def insert_data(self, data):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/6 21:19
        @updateTime(upf): 2021/5/6 21:19
        """
        return await self.mongodb.collection.insert_one(data)
    
    async def query_all_data(self):
        """
        @func name: 
        @desc: 
        @author: SAM
        @createTime: 2021/5/6 22:33
        @updateTime(upf): 2021/5/6 22:33
        """
        data = self.mongodb.collection.find()
        return data
