# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Settings
# CreateTime: 2021/4/25 19:36
# Summary: 'tornado setting 文件'


from conf import CONF

settings = {
    'template_path': CONF.settings.template_path,
    'static_path': CONF.settings.static_path,
    'static_url_prefix': CONF.settings.static_url_prefix,
    'cookie_secret': CONF.settings.cookie_secret,
    'xsrf_cookies': CONF.settings.xsrf_cookies,
    'debug': CONF.settings.debug,
    # 'autoreload': CONF.settings.autoreload,
    # 'ui_methods': CONF.settings.ui_methods,
}
