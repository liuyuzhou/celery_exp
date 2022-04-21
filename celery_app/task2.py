# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 2:23 PM
# @Author   : YuzhouLiu
# @FileName : task2.py
# @Describe : 
=================================================="""
import time

from celery_app import app


@app.task
def multiply(x, y):
    time.sleep(2)
    return x * y
