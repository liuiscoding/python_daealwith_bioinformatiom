# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/6 17:11
@Author  : lhd - l17354000520@163.com
@FileName: formatFasta.py
@Software: PyCharm
'''
'''
读入test3.fa，把每条FASTA序列分割成80个字母一行的序列
'''
from Bio import Seq
from Bio import SeqIO
file='test3.fa'
for record in SeqIO.parse(file,'fasta'):
    # print(record.seq)
    print('>'+record.id)
    length=len(record.seq)
    for line in range(0,length,80):
        print(record.seq[line:line+80])

