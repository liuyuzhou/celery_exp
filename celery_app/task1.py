# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 2:23 PM
# @Author   : YuzhouLiu
# @FileName : task1.py
# @Describe : 
=================================================="""
import time

from celery_app import app


@app.task
def add(x, y):
    time.sleep(10)
    return x + y
