# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 2:50 PM
# @Author   : YuzhouLiu
# @FileName : celery_config.py
# @Describe : 
=================================================="""
# -*- coding: utf-8 -*-

from datetime import timedelta

from celery.schedules import crontab

# Broker and Backend
BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

# Timezone
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，不指定默认为 'UTC'
# CELERY_TIMEZONE='UTC'

# import
CELERY_IMPORTS = (
    'celery_beat.task1',
    'celery_beat.task2'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-10-seconds': {
        'task': 'celery_beat.task1.add',
        'schedule': timedelta(seconds=10),  # 每 10 秒执行一次
        'args': (5, 8)  # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_beat.task2.multiply',
        'schedule': crontab(hour=9, minute=50),  # 每天早上 9 点 50 分执行一次
        'args': (3, 7)  # 任务函数参数
    }
}
