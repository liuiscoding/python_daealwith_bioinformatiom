# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/6 9:27
@Author  : lhd - l17354000520@163.com
@FileName: module.py
@Software: PyCharm
'''
import os
# print(os.getcwd())

#命令行参数
# import sys
# a=sys.argv[0]
# b=sys.argv[1]
# c=sys.argv[2]
# print(f'filename:{a}')
# print(f'参数1:{b}')
# print(f'参数2:{c}')

#命令行参数读取文件
# import sys
# def read_file(filename):
#     for line in open(filename):
#         print(line)
# read_file(sys.argv[1])   #注意这里是1不是0，和perl语言参数不一样的规则


#生成程序帮助
import sys
from optparse import OptionParser
pro=sys.argv[0]
usage = f"usage: python {pro} [options]"
parser = OptionParser(usage=usage)
parser.add_option("-f", "--file", dest="filename",
                  help="read data from filename", metavar="FILE")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose")
(options, args) = parser.parse_args()
