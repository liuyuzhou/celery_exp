# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 3:33 PM
# @Author   : YuzhouLiu
# @FileName : tasks_email.py
# @Describe : 
=================================================="""
# tasks.py
import time

from celery import Celery

# 申明获取task来源以及消费者执行task结果的redis
broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

app = Celery('my_task', broker=broker, backend=backend)


@app.task
def add(x, y):
    print(f"开始执行时间为：{time.time()}")
    time.sleep(5)  # 模拟耗时操作
    print(f"结束执行时间为：{time.time()}")
    return x + y


@app.task
def push_email(name):
    print(f"准备给 {name}发送邮件！")
    time.sleep(5)
    print(f"邮件发送完成！")
    return True
