# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: HomeController
# CreateTime: 2021/4/27 21:59
# Summary: ''


import tornado.auth
import ast
import json
from backend.core.Basehandler import BaseHandler
from backend.core.RouteHandler import Route
from backend.utils.Decorate import Return
from service.SourceDataService import SourceDataService


@Route(r'/')
class HomeHandler(BaseHandler, tornado.auth.GoogleOAuth2Mixin):
    """
    @interface name:
    @desc:
    @author: SAM
    @createTime: 2021/4/27 22:01
    @updateTime(upf): 2021/4/27 22:01
    """

    @Return
    async def get(self):
        user = None
        json_dict = self.json_dict
        user_name = self.get_argument('user', default=False)
        if user_name:
            # await self.get_authenticated_user(http_client=None)
            user = await self.get_authenticated_user(
                redirect_uri='www.baidu.com',
                code=self.get_argument('code')
            )
        else:
            self.authorize_redirect(
                redirect_uri='www.baidu.com',
                client_id='asdf',
                response_type='code',
                extra_params={'approval_prompt': 'auto'}
            )
        print(user)

        # sourceDataService = SourceDataService()
        # result = await sourceDataService.insert_source_data_service(doc)
        # if result:
        #     ...
        # else:  # 插入失败
        #     ...
        # return self.write(json.dumps(doc))

        # return ReturnJson.SUCCESS(data=result)


@Route('/home')
class WithDrawHandler(BaseHandler):
    """
    @interface name:
    @desc:
    @author: SAM
    @createTime: 2021/5/6 20:59
    @updateTime(upf): 2021/5/6 20:59
    """

    @Return
    async def get(self):
        sourceService = SourceDataService()
        read_line = None
        with open('D:\Projects\Python\Local\Forecast500\statics\win_num.txt', 'r') as f:
            file = f.readlines()
            # item = file[0]
            # item = tuple(int(x) for x in ast.literal_eval(item))
            # ret = await sourceService.withdraw_data_from_txt(item)
            for item in file:
                item = tuple(int(x) for x in ast.literal_eval(item))
                await sourceService.withdraw_data_from_txt(item)
        print('ret: ', '上传处理成功!')
        return self.write(json.dumps({'ret: ', '上传处理成功!'}))


@Route('/all')
class FindAllDataHandler(BaseHandler):
    """
    @interface name:
    @desc:
    @author: SAM
    @createTime: 2021/5/7 19:19
    @updateTime(upf): 2021/5/7 19:19
    """

    @Return
    async def get(self):
        sourceService = SourceDataService()
        # all_data = await sourceService.find_all_data()
        return await sourceService.find_all_data()
