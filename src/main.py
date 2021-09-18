#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


import sys
import jieba
import re
import gensim


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


def calc_similarity(text1, text2):
    """
    计算余弦相似度
    :param text1: 文本1
    :param text2: 文本2
    :return: 相似度
    """
    texts = [text1, text2]
    # 建立词袋模型向量化文本
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))  # 计算余弦相似度
    test_corpus = dictionary.doc2bow(text1)     # 将文本转换为bow向量
    cosine_sim = similarity[test_corpus][1]    # 变量类型为<class 'numpy.float32'>
    result = round(cosine_sim.item(), 2)   # 转化为<class 'float'>，并取小数点后两位
    return result


if __name__ == '__main__':
    try:
        original_path, check_path, answer_path = sys.argv[1: 4]
    except ValueError as e:     # 未传参则会引发ValueError
        print(e)
        print("请使用命令行给出参数")
        sys.exit(-1)

    text1 = filter_words(read_file(original_path))
    text2 = filter_words(read_file(check_path))
    print(calc_similarity(text1, text2))
