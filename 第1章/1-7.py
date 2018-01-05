# 如何根据字典中值的大小，对字典中的项排序

# 案列：某班英语成绩以字典形式存储为:{'lucy':88,'bob':66...},根据成绩高低，计算学生排名

"""
方法:使用内置的sorted()函数
	1. 利用zip()将字典转换成元组
	2. 传递sorted函数的key参数
"""

"""
1. 先生成一个有6个学生，分数随机的字典
2. 通过zip函数，把字典的values和keys组合成一个元组,然后通过sorted函数排序
3. 利用sorted函数中的key参数 

In [1]: from random import randint

In [2]: student = {x:randint(0,100) for x in 'xyzabc'}

In [3]: student
Out[3]: {'a': 66, 'b': 24, 'c': 33, 'x': 15, 'y': 54, 'z': 19}

In [7]: student.keys()
Out[7]: dict_keys(['x', 'y', 'z', 'a', 'b', 'c'])

In [8]: student.values()
Out[8]: dict_values([15, 54, 19, 66, 24, 33])

In [9]: sorted(zip(student.values(), student.keys()))
Out[9]: [(15, 'x'), (19, 'z'), (24, 'b'), (33, 'c'), (54, 'y'), (66, 'a')]

In [10]: student.items()
Out[10]: dict_items([('x', 15), ('y', 54), ('z', 19), ('a', 66), ('b', 24), ('c', 33)])

In [11]: sorted(student.items(), key=lambda x:x[1])
Out[11]: [('x', 15), ('z', 19), ('b', 24), ('c', 33), ('y', 54), ('a', 66)]
"""