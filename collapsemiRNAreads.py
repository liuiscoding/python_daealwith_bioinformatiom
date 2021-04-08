# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/7 20:54
@Author  : lhd - l17354000520@163.com
@FileName: collapsemiRNAreads.py.py
@Software: PyCharm
'''
'''
转换smRNA-Seq的测序数据
输出文件格式 (mir.collapse.fa, 名字的前3个字母为样品的特异标示，
中间的数字表示第几条序列，是序列名字的唯一标示，第三部分是x加每个reads被测到的次数。
三部分用下划线连起来作为fasta序列的名字。)
'''
dictSeq={}
head=1
for item in open('mir.collapse.txt'):
    # print(item)
    if head:
        head=head-1
        continue
    # print(item)
    line=item.strip().split('\t')
    # print(line)
    sequence=line[0]
    count=line[1]
    # print(sequence)
    # print(count)
    dictSeq[sequence]=count
# print(dictSeq)
new_count=0
for key,value in dictSeq.items():
    # print(key,value)
    new_count+=1
    print(f'>ESB_{new_count}_x{value}')
    # print(new_count)
    print(key)




