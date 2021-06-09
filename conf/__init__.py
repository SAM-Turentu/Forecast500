# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: __init__.py
# CreateTime: 2021/4/21 22:25
# Summary: '读取配置文件'


from oslo_log import log as logging
from oslo_config import cfg, types

CONF = cfg.CONF

# # region Tornado Log
# log_group = cfg.OptGroup('log', title='Tornado log 配置')
# CONF.register_group(log_group)
# CONF.register_cli_opts([
#     cfg.BoolOpt('False', default=False),
#     cfg.StrOpt('log_file', default='tornado_main.log'),
#     cfg.StrOpt('log_dir', default='./logs'),
#     cfg.StrOpt('log_rotate_interval_type', default='Minutes'),
#     cfg.IntOpt('log_rotate_interval', default=1),
#     cfg.StrOpt('log_rotation_type', default='interval'),
# ], log_group)
# # endregion
#
#
# # region 日志配置
# log = logging.getLogger(__name__)
# logging.register_options(CONF)
# CONF.log_file = CONF.log.log_file
# CONF.log_dir = CONF.log.log_dir
# CONF.log_rotate_interval_type = CONF.log.log_rotate_interval_type
# CONF.log_rotate_interval = CONF.log.log_rotate_interval
# CONF.log_rotation_type = CONF.log.log_rotation_type
# logging.setup(CONF, 'Forecast500')
# # endregion


# region Project Host And Port
project_group = cfg.OptGroup(name='dd', title="project 地址配置")
CONF.register_group(project_group)
CONF.register_cli_opts([
    cfg.StrOpt('host', default='0.0.0.0'),
    cfg.IntOpt('port', default=8001, min=1024, max=65535),
], project_group)
# endregion


# region MongoDB
mongodb_group = cfg.OptGroup(name='mongodb', title="mongodb 配置")
CONF.register_group(mongodb_group)
CONF.register_cli_opts([
    cfg.StrOpt('host', default='0.0.0.0'),
    cfg.IntOpt('port', default=27017, min=1024, max=65535),
], mongodb_group)
# endregion


# region MySQL
mysql_group = cfg.OptGroup(name='mysql', title="MySQL DSN配置")
CONF.register_group(mysql_group)
CONF.register_cli_opts([
    cfg.StrOpt('host', default='0.0.0.0'),
    cfg.IntOpt('port', default=3306, min=1024, max=65535),
    cfg.StrOpt('user', default=''),
    cfg.StrOpt('password', default=''),
    cfg.StrOpt('database', default=''),
], mysql_group)
# endregion


# region Tornado Setting
settings_group = cfg.OptGroup('settings', title='Tornado settings 配置')
CONF.register_group(settings_group)
CONF.register_cli_opts([
    cfg.StrOpt('template_path', default='default'),
    cfg.StrOpt('static_path', default='default'),
    cfg.StrOpt('static_url_prefix', default='default'),
    cfg.StrOpt('cookie_secret', default='default'),
    cfg.BoolOpt('xsrf_cookies', default=False),
    cfg.BoolOpt('debug', default=False),
    cfg.BoolOpt('autoreload', default=False),
    # cfg.StrOpt('ui_methods', default='default'),
], settings_group)
# endregion


# 在项目启动命令中添加配置模式：开发(dev)，测试(uat)，生产(prod)
# 项目启动命令添加下面命令，不添加则默认dev环境
# --config-file=conf\\dev.ini
# --config-file=conf\\uat.ini
# --config-file=conf\\prod.ini

CONF(default_config_files=['conf\\dev.ini'])
