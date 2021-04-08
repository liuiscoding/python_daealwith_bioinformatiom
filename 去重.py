# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/6 9:15
@Author  : lhd - l17354000520@163.com
@FileName: 元组.py
@Software: PyCharm
'''

#去重
# list=[3,4,5,3]
# new_tuple=set(list)
# print(type(new_tuple))
# print(new_tuple)

#集合（含有自动去重功能）
tuple=set()
print(type(tuple))
tuple.add(1)
tuple.add(2)
tuple.add(3)
tuple.add(1)
print(tuple)