# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/6 20:29
@Author  : lhd - l17354000520@163.com
@FileName: transferMultipleColumToMatrix.py.py
@Software: PyCharm
'''
'''
将文件(multipleColExpr.txt)中基因在多个组织中的表达数据转换为矩阵形式
'''
file='multipleColExpr.txt'
head=1
dict={}
aggregate=set()  #创建一个集合
for line in open(file):
    if head:   #跳过首行
        head=head-1
        continue
    lineList=line.split('\t')
    # print(lineList)
    gene=lineList[0]
    tissue=lineList[1]
    aggregate.add(tissue)
    expr=lineList[2]
    if gene not in dict:
        dict[gene]={}
    assert tissue not in dict[gene]
    dict[gene][tissue] = expr  # 字典的嵌套，注意这里的缩进，缩进错误会导致结果嵌套的字典数据包缺失
# print(dict)
tissueList=list(aggregate)  #集合转换为列表方便排序
tissueList.sort()
# print(tissueList)
print('Gene\t'+'\t'.join(tissueList))
for gene,tissueDict in dict.items():
    # print(tissueDict)
    exprList=[gene]
    for new_tissue in tissueList:
        exprList.append(tissueDict[new_tissue])  #添加输出结果到列表，最后\t连字符连接起来
        # print(exprList)
    print('\t'.join(exprList))