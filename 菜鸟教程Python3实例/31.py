# Python list 常用操作

"""
1. list定义

In [1]: li = ['a', 'b', 'c', 'd', 'e']

In [2]: li
Out[2]: ['a', 'b', 'c', 'd', 'e']

In [3]: li[0]
Out[3]: 'a'

"""

"""
2.list 负数索引

In [4]: li[-1]
Out[4]: 'e'

In [5]: li[::2]
Out[5]: ['a', 'c', 'e']

In [6]: li[-2:]
Out[6]: ['d', 'e']

In [7]: li[:2]
Out[7]: ['a', 'b']
"""

"""
3.list 增加元素

In [8]: li
Out[8]: ['a', 'b', 'c', 'd', 'e']

In [9]: li.append('new')

In [10]: li
Out[10]: ['a', 'b', 'c', 'd', 'e', 'new']

In [11]: li.insert(2, 'new')

In [12]: li
Out[12]: ['a', 'b', 'new', 'c', 'd', 'e', 'new']

In [13]: li.extend(['one', 'two'])

In [14]: li
Out[14]: ['a', 'b', 'new', 'c', 'd', 'e', 'new', 'one', 'two']
"""

"""
4.list 搜索

In [15]: li
Out[15]: ['a', 'b', 'new', 'c', 'd', 'e', 'new', 'one', 'two']

In [16]: li.index('one')
Out[16]: 7

In [17]: li.index('g')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-17-67ad8e3683b7> in <module>()
----> 1 li.index('g')

ValueError: 'g' is not in list
"""

"""
5.list 删除元素

In [18]: li
Out[18]: ['a', 'b', 'new', 'c', 'd', 'e', 'new', 'one', 'two']

In [19]: li.remove('new')   # 删除的是第一个`new`

In [20]: li
Out[20]: ['a', 'b', 'c', 'd', 'e', 'new', 'one', 'two']

In [21]: li.pop()   # 删除list最后一个元素
Out[21]: 'two'

In [22]: li
Out[22]: ['a', 'b', 'c', 'd', 'e', 'new', 'one']
"""

"""
6.list 运算符

In [23]: li = ['a', 'b', 'c']

In [24]: li = li + ['one', 'two']

In [25]: li
Out[25]: ['a', 'b', 'c', 'one', 'two']
"""

"""
7.使用join链接list成为字符串

In [26]: li
Out[26]: ['a', 'b', 'c', 'one', 'two']

In [27]: ''.join(li)
Out[27]: 'abconetwo'

In [28]: ':'.join(li)
Out[28]: 'a:b:c:one:two'
"""

"""
8.list 分割字符串

In [29]: li
Out[29]: ['a', 'b', 'c', 'one', 'two']

In [30]: s = ':'.join(li)

In [31]: s
Out[31]: 'a:b:c:one:two'

In [32]: s.split(':')
Out[32]: ['a', 'b', 'c', 'one', 'two']

In [33]: s.split(':',2)
Out[33]: ['a', 'b', 'c:one:two']
"""

"""
9.list 的映射解析

In [34]: li = [1, 2, 3, 4, 5]

In [35]: [x*2 for x in li]
Out[35]: [2, 4, 6, 8, 10]
"""

"""
10.dictionary中的解析

In [36]: d = {'a':1, 'b':2 , 'c':3, 'd':4, 'e':5}

In [37]: d.keys()
Out[37]: dict_keys(['a', 'b', 'c', 'd', 'e'])

In [38]: d.values()
Out[38]: dict_values([1, 2, 3, 4, 5])

In [39]: d.items()
Out[39]: dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

In [40]: [k for k in d.items()]
Out[40]: [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

In [41]: [v for k,v in d.items()]
Out[41]: [1, 2, 3, 4, 5]

In [42]: ['%s=%d' % (k,v) for k,v in d.items()]
Out[42]: ['a=1', 'b=2', 'c=3', 'd=4', 'e=5']
"""

"""
11.list 过滤

In [45]: li
Out[45]: ['a', 'ds', 'b', 'a', 'b', 'dsa']

In [46]: [x for x in li if len(x) > 1]
Out[46]: ['ds', 'dsa']

In [47]: [x for x in li if len(x) != 'b']
Out[47]: ['a', 'ds', 'b', 'a', 'b', 'dsa']

In [48]: [x for x in li if li.count(x) == 1]  # 返回列表中只出现一次的元素
Out[48]: ['ds', 'dsa']

In [49]: li.count?
Docstring: L.count(value) -> integer -- return number of occurrences of value
Type:      builtin_function_or_method
"""