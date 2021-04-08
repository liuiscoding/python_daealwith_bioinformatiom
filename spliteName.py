# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/6 17:02
@Author  : lhd - l17354000520@163.com
@FileName: spliteName.py
@Software: PyCharm
'''
'''
写程序 splitName.py, 读入test2.fa, 并取原始序列名字第一个空格前的名字为处理后的序列名字，输出到屏幕
'''
for line in open('test2.fa'):
    if line.startswith('>'):
        list=line.split(' ')
        # print(list)
        print(list[0])
    else:
        print(line,end='')