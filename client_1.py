# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 2:15 PM
# @Author   : YuzhouLiu
# @FileName : client_1.py
# @Describe : 
=================================================="""
# -*- coding: utf-8 -*-

from tasks import add

# 异步任务
result = add.delay(2, 8)

print('hello world')

print(result.get())
