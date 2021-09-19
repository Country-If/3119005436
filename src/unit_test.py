#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

import unittest
import os


class Test(unittest.TestCase):
    orig_path = "../data/test1/orig.txt"
    ans_path = "answer.txt"

    def test_add1(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test1/orig_0.8_add.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_del1(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test1/orig_0.8_del.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_dis_1_1(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test1/orig_0.8_dis_1.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_dis10_1(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test1/orig_0.8_dis_10.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_dis15_1(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test1/orig_0.8_dis_15.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_add2(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test2/orig_0.8_add.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_del2(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test2/orig_0.8_del.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_dis_1_2(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test2/orig_0.8_dis_1.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_dis10_2(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test2/orig_0.8_dis_10.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)

    def test_dis15_2(self, orig_path=orig_path, ans_path=ans_path):
        test_path = "../data/test2/orig_0.8_dis_15.txt"
        os.system('python main.py ' + orig_path + ' ' + test_path + ' ' + ans_path)


if __name__ == '__main__':
    unittest.main()
