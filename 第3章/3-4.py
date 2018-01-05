# 如何将多个小字符串拼接橙一个大的字符串？

"""
案例:
在程序中我们将各个参数按次序收集到列表中：
["<0112>", "<32>", "<1024*768>", "<60>", "<220>", "<500>"]
最终我们要把各个参数拼成一个字符串发送出去
"<0112>, <32>, <1024*768>, <60>, <220>, <500>"

解决方法:
1. 迭代列表，将每个字符串'+'起来
2.str.join()   ---推荐
"""

"""
In [10]: str.join?
Docstring:
S.join(iterable) -> str

Return a string which is the concatenation of the strings in the
iterable.  The separator between elements is S.
Type:      method_descriptor

In [12]: ':'.join(['abc', '123', 'xyz'])
Out[12]: 'abc:123:xyz'

In [13]: ''.join(['abc', '123', 'xyz'])
Out[13]: 'abc123xyz'

In [15]: L = ['abc', 123, 'xyz', 456]

In [16]: ''.join(str(x) for x in L)
Out[16]: 'abc123xyz456'
"""