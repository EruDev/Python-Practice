# 如何对字符串进行左、右、居中对齐？

"""
案例:
某个字典存储了一系列属性值,
{
	'lodDist':100.0,
	'SmallCull':0.04,
	'Ddasd':21.2,
	'dsa':31.0
}
在程序中，我们想以以下工整的格式将其内容输出，如何处理？
lodDist   :100.0,
SmallCull :0.04,
Ddasd     :21.2,
dsa       :31.0

解决方法:
1.使用字符串中的str.ljust()、str.center()、str.rjust()
2.format方法
"""

"""
In [1]: s = 'abc'

In [2]: s.ljust?
Docstring:
S.ljust(width[, fillchar]) -> str

Return S left-justified in a Unicode string of length width. Padding is
done using the specified fill character (default is a space).
Type:      builtin_function_or_method

In [3]: s.ljust(20)
Out[3]: 'abc                 '

In [4]: s.ljust(20, '=')
Out[4]: 'abc================='

In [5]: s.rjust(20)
Out[5]: '                 abc'

In [6]: len(s.rjust(20))
Out[6]: 20

In [7]: s.center(20)
Out[7]: '        abc         '

In [8]: format?
Signature: format(value, format_spec='', /)
Docstring:
Return value.__format__(format_spec)

format_spec defaults to the empty string
Type:      builtin_function_or_method

In [9]: format(s, '<20')
Out[9]: 'abc                 '

In [10]: format(s, '>20')
Out[10]: '                 abc'

In [11]: format(s, '^20')
Out[11]: '        abc         '

"""

"""
看这里，这个例子重要

In [29]: d = {
    ...:     'lodDist':100.0,
    ...:     'SmallCull':0.04,
    ...:     'Ddasd':21.2,
    ...:     'dsa':31.0
    ...: }

In [30]: d.keys()
Out[30]: dict_keys(['lodDist', 'SmallCull', 'Ddasd', 'dsa'])

In [31]: list(map(len, d.keys()))  # 根据Len得到字典中键,并存到一个List
Out[31]: [7, 9, 5, 3]

In [32]: max(list(map(len, d.keys()))) # 得到最大的键的长度
Out[32]: 9

In [33]: w = max(list(map(len, d.keys())))  # 用一个w来接收

In [34]: for k in d:
    ...:     print(k.ljust(w), ':', d[k])  # 字典中的key,按照左对齐(w就是字典中最大的那个键的长度)，然后打印字典的值
    ...:
lodDist   : 100.0
SmallCull : 0.04
Ddasd     : 21.2
dsa       : 31.0

"""