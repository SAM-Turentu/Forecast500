# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: get_ip
# CreateTime: 2022/7/6 20:22
# Summary: ''


from lxml import etree
from backend.utils.http_request.http_request import HttpRequest


class GetIP(object):

    def __init__(self):
        self.http_request = HttpRequest()
        self.base_url = 'https://www.zdaye.com/'
        self.url = 'https://www.zdaye.com/dayProxy/ip/333553.html'

    def get_ip_url_list_10(self, start=None, end=None, nums=10):
        start = start or 332553
        end = end or 333553

        url_format = "https://www.zdaye.com/dayProxy/ip/{times}.html"
        url_list_10 = []
        for _ in range(nums):
            url = url_format.format(times=end)
            url_list_10.append(url)
            if end < start:
                break
            end = end - 1
        return url_list_10

    def response(self):
        url_list = self.get_ip_url_list_10()
        for url in url_list:
            response = self.http_request.get_reponse(url)
            text = response.text
            self.parse(text)

    def parse(self, text):
        html = etree.HTML(text)


if __name__ == '__main__':
    get_ip = GetIP()
    get_ip.response()
