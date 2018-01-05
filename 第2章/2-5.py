
# 如何在一个for语句中迭代多个可迭代对象？

"""
案例子:
1. 某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，
同时迭代三个列表，计算每个学生的总分（并行）
2. 某年级有4个班，某次考试没办英语成绩分别存储在4个列表中，
依次迭代每个列表，统计全学年成绩高于90分人数(串行)

解决方案:
1.并行--使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
2.串行--使用标准库itertools.chain,它能将多个可迭代对象连接
"""

"""
1. 先随机生成语文、数学、英语这个三个列表。
然后利用zip函数，将每个学生的三门成绩加起来，存在一个列表中
打印列表
In [2]: chinese = [randint(1,100) for _ in range(40)]

In [4]: math = [randint(1,100) for _ in range(40)]

In [5]: english = [randint(1,100) for _ in range(40)]

In [6]: total = []

In [9]: for c,m,e in zip(chinese, math, english):
   ...:     total.append(c+m+e)
   ...:

In [10]: total
...
"""

"""
2. 先创建四个班级的英语成绩，分别存在c1~c4列表中，
然后利用itertools下的chain，把四个列表串联起来，求出分数大于80的人数

In [11]: from itertools import chain

In [12]: chain?
Init signature: chain(self, /, *args, **kwargs)
Docstring:
chain(*iterables) --> chain object

Return a chain object whose .__next__() method returns elements from the
first iterable until it is exhausted, then elements from the next
iterable, until all of the iterables are exhausted.
Type:           type

In [13]: from random import randint

In [14]: c1 = [randint(1,100) for _ in range(40)]

In [15]: c2 = [randint(1,100) for _ in range(43)]

In [16]: c3 = [randint(1,100) for _ in range(41)]

In [17]: c4 = [randint(1,100) for _ in range(39)]

In [18]: count = 0

In [19]: for i in chain(c1, c2, c3, c4):
    ...:     if i > 80:
    ...:         count += 1
    ...:

In [20]: count
Out[20]: 34
"""
