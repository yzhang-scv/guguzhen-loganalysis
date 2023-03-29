#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/3/29 10:28
# @Author : chaocai

import yaml


# 初始化加载yaml配置文件
def _init():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        global config_data
        config_data = yaml.safe_load(f)


# 读取配置文件的值
def read_config(key):
    return config_data.get(key)
