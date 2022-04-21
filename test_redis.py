# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 3:34 PM
# @Author   : YuzhouLiu
# @FileName : test_redis.py
# @Describe : 
=================================================="""
# test_redis.py (查看中间件中的剩余任务个数)
from redis import Redis

r = Redis(host="127.0.0.1", port=6379, db=1)
# r = Redis(host="10.50.255.104", port=6379, db=1)

task_list = r.lrange("celery", 0, -1)
print(f"任务个数：{len(task_list)}")

# for i in task_list:
# 	print(i)
