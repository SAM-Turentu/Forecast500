# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Basehandler
# CreateTime: 2021/5/5 16:59
# Summary: ''


import json
from asyncio import Future
from typing import Optional, Awaitable, Union, Any
from tornado.web import RequestHandler

from backend.utils.Result import ReturnJson
from backend.utils.Utils import Utils


class BaseHandler(RequestHandler):

    def __init__(self, application, request, **kwargs):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/5 17:02
        @updateTime(upf): 2021/5/5 17:02
        """

        self.json_dict = None
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def set_default_headers(self) -> None:
        """
        @func name: 设置 headers
        @desc:
        @author: SAM
        @createTime: 2021/5/6 19:41
        @updateTime(upf): 2021/5/6 19:41
        """
        self.set_header('Access-Control-Allow-Origin', '*')
        # self.set_header('Access-Control-Allow-Origin', 'http://www.forecast500.com/')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def initialize(self) -> None:
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/5 17:07
        @updateTime(upf): 2021/5/5 17:07
        """
        ...

    def prepare(self) -> Optional[Awaitable[None]]:
        """
        @func name: 预处理
        @desc: 在请求方式的HTTP方法前先执行
        @author: SAM
        @createTime: 2021/5/5 17:02
        @updateTime(upf): 2021/5/5 17:02
        """
        content_type = self.request.headers.get('Content-Type', '')
        user_agent = self.request.headers.get('User-Agent')
        if content_type.startswith('application/json'):
            self.json_dict = json.loads(self.request.body)

        token = self.request.headers.get('Authorization')
        # 处理token 权限判断等，请求方法前的一些处理

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        """
        @func name:
        @desc: 方法发生异常时，可收集系统异常日志，并返回前端需要的格式数据
        @author: SAM
        @createTime: 2021/5/5 17:06
        @updateTime(upf): 2021/5/5 17:06
        """
        exc_cls, exc_instance, trace = kwargs.get('exc_info')
        if status_code != 200:
            self.set_status(status_code)
            self.write(ReturnJson.exception(message=exc_instance))

    def on_finish(self) -> None:
        """
        @func name:
        @desc: 最后执行的方法  例：释放资源等
        @author: SAM
        @createTime: 2021/5/5 17:03
        @updateTime(upf): 2021/5/5 17:03
        """
        ...

    def json(self, result):
        """
        @func name: 转换为json格式返回接口数据
        @desc:
        @author: SAM
        @createTime: 2021/5/5 17:15
        @updateTime(upf): 2021/5/5 17:15
        """
        self.write(json.dumps(result, cls=Utils.JSONEncoder(), sort_keys=False))
        self.finish()
