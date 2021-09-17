#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


import sys


def read_file(file_path):
    """
    读取指定路径下的文件，以字符串形式返回文件内容
    :param file_path: 文件路径
    :return: 字符串
    """
    string = ""    # 初始化空字符串
    f = open(file_path, 'r', encoding='UTF-8')  # 以只读形式读取文件
    # 逐行读取文件并存储为字符串
    line = f.readline()
    while line:
        if line != '\n':    # 过滤空行
            string = string + line
        line = f.readline()
    f.close()       # 释放内存
    return string


if __name__ == '__main__':
    try:
        original_path, check_path, answer_path = sys.argv[1: 4]
    except Exception as e:
        print(e)
        print("请使用命令行给出参数")
        sys.exit(-1)

    file_str = read_file(original_path)
    print(file_str)
