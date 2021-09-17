#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


import sys
import jieba
import re


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


def filter_words(string):
    """
    将给定字符串进行分词，以列表形式返回结果
    :param string: 目标字符串
    :return: 列表
    """
    words = jieba.cut(string)       # 使用jieba库进行分词
    result = []
    for word in words:
        if re.match(r'[a-zA-Z0-9\u4e00-\u9fa5]', word):     # 正则表达式匹配中英文和数字
            result.append(word)
    return result


if __name__ == '__main__':
    try:
        original_path, check_path, answer_path = sys.argv[1: 4]
    except Exception as e:
        print(e)
        print("请使用命令行给出参数")
        sys.exit(-1)

    file_str = read_file(original_path)
    # print(file_str)
    filter_result = filter_words(file_str)
    print(filter_result)
