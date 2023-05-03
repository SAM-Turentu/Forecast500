# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Settings
# CreateTime: 2021/4/25 19:36
# Summary: 'tornado setting 文件'
import os

from conf import CONF

settings = {
    'template_path': CONF.settings.template_path,
    'static_path': CONF.settings.static_path,
    'static_url_prefix': CONF.settings.static_url_prefix,
    'cookie_secret': CONF.settings.cookie_secret,
    'xsrf_cookies': CONF.settings.xsrf_cookies,
    'debug': CONF.settings.debug,
    'google_oauth': {'key': 'google_oauth_sam', 'secret': 'secret'},
    # 'secret_jwt': 'secret_jwt-SAM-Turentu',
    # 'autoreload': CONF.settings.autoreload,
    # 'ui_methods': CONF.settings.ui_methods,
}
# SETTINGS = {
#     "debug":True,
#     "template_path":os.path.join(os.path.dirname(__file__),"templates"),
#     "static_url_prefix":"/static/",
# }