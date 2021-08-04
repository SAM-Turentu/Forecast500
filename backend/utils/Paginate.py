# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Paginate
# CreateTime: 2021/7/23 15:19
# Summary: ''


class Pagination:

    def __init__(self, page=1, pages=1, col=10, total=0):
        """
        @Author: SAM
        @CreateTime: 2021/7/23 13:00
        @UpdateTime(upf): 2021/7/23 13:00
        @Desc: ''
        :param page: 当前页
        :param pages: 总页数
        :param col: 每页显示数据条数
        :param total: 总数据量
        """

        self.page = page  # 当前页
        self.pages = pages  # 总页数
        self.col = col  # 每页显示数据条数
        self.total = total  # 总数据量
        if self.page < 1:
            self.page = 1
        if self.col not in [5, 10, 20, 30]:
            self.col = 10

        # 计算总页数
        pages, tmp = divmod(self.total, self.col)
        self.pages = pages + 1 if tmp > 0 else pages

