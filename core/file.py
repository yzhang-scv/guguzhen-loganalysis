#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/3/29 10:28
# @Author : chaocai

import json
import os

from core import config


# 加载数据，批量加载合并排序
def file_load():
    result_list = []
    input_path = config.read_config('input_path')
    for file_name in os.listdir(input_path):
        if file_name != 'pc.txt':
            file_path = input_path + file_name
            with open(file_path, encoding='utf-8') as f:
                read = f.read()
                try:
                    data_list = json.loads(read)['data']['data'][0]['rows']
                    result_list.extend(data_list)
                except:
                    pass
    # 时间排序
    return sorted(result_list, key=lambda x: (x['time']))


# 删除输出文件
def del_file(path):
    if os.path.isfile(path):
        os.remove(path)


# 输出结果
def write_data(result_map):
    print('输出对手数量：%s' % len(result_map))
    with open(config.read_config('output_path'), 'a', encoding='utf-8') as f:
        f.write('PC\n')
    for key in result_map:
        with open(config.read_config('output_path'), 'a', encoding='utf-8') as f:
            f.write(result_map[key])
    with open(config.read_config('output_path'), 'a', encoding='utf-8') as f:
        f.write('ENDPC')