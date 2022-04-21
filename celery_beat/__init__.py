# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 2:27 PM
# @Author   : YuzhouLiu
# @FileName : __init__.py.py
# @Describe : 
=================================================="""
# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('demo2')
app.config_from_object('celery_beat.celery_config')
