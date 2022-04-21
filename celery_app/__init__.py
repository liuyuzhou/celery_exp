# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 2:22 PM
# @Author   : YuzhouLiu
# @FileName : __init__.py.py
# @Describe : 
=================================================="""
# -*- coding: utf-8 -*-

from celery import Celery

# 创建 Celery 实例
app = Celery('demo1')
# 通过 Celery 实例加载配置模块
app.config_from_object('celery_app.celery_config')
