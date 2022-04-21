# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 2:51 PM
# @Author   : YuzhouLiu
# @FileName : task1.py
# @Describe : 
=================================================="""
import time

from celery_beat import app


@app.task
def add(x, y):
    time.sleep(2)
    return x + y
