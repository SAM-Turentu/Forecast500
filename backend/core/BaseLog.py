# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BaseLog
# CreateTime: 2021/6/7 10:32
# Summary: ''


import tornado.log


class LogFormatter(tornado.log.LogFormatter):

    def __init__(self):
        """
        @author: SAM
        @CreateTime: 2021/6/7 11:11
        @UpdateTime(upf): 2021/6/7 11:11
        @desc: ''
        """
        super(LogFormatter, self).__init__(
            fmt='%(color)s[%(asctime)s %(module)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            color=True,
        )

#   时间           线程名                 日志等级            执行行号      内容消息
# %(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] [%(lineno)d]  %(message)s


#              日志等级           时间       模块       执行行数                  内容消息
# %(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s

# [2016-08-07 09:38:01   执行文件名:    执行函数名:   执行行数    日志等级]                    内容消息
# %(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s

#     %(name)s            Name of the logger (logging channel)
#     %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
#                         WARNING, ERROR, CRITICAL)
#     %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
#                         "WARNING", "ERROR", "CRITICAL")
#     %(pathname)s        Full pathname of the source file where the logging
#                         call was issued (if available)
#     %(filename)s        Filename portion of pathname
#     %(module)s          Module (name portion of filename)
#     %(lineno)d          Source line number where the logging call was issued
#                         (if available)
#     %(funcName)s        Function name
#     %(created)f         Time when the LogRecord was created (time.time()
#                         return value)
#     %(asctime)s         Textual time when the LogRecord was created
#     %(msecs)d           Millisecond portion of the creation time
#     %(relativeCreated)d Time in milliseconds when the LogRecord was created,
#                         relative to the time the logging module was loaded
#                         (typically at application startup time)
#     %(thread)d          Thread ID (if available)
#     %(threadName)s      Thread name (if available)
#     %(process)d         Process ID (if available)
#     %(message)s         The result of record.getMessage(), computed just as
#                         the record is emitted
