# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""=================================================
# @Time     : 2022/4/10 3:33 PM
# @Author   : YuzhouLiu
# @FileName : producer.py
# @Describe : 
=================================================="""
import random

# 定义生产者 producer.py
from tasks_email import add, push_email


def do_add(x, y):
    res = add.delay(x, y)
    print(res.id)
    return {"code": 200, "mag": "success"}


def registered():
    name = input("请输入注册人员名称：")
    push_email.delay(name)
    return {"code": 200, "msg": f"恭喜{name}注册成功! 请查看邮箱点击确认链接进行校验。"}


if __name__ == '__main__':
    # 这里产生 100 个 task；
    for i in range(100):
        print(do_add(random.randint(1, 1000000), random.randint(1000000, 2000000)))
    # 这里再新加一个 task
    print(registered())
