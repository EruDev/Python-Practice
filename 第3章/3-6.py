# 如何去掉字符串中不需要的字符？

"""
案例:
1.过滤掉用户输入前后多余的空白字符: 
' zhangsan@qq.com '
2. 过滤某windows下编辑文本中的'\r':
'hello world \r\n'
3. 去掉文本中的unicode组合符号:
u''

解决方法:
1. strip()、lstrip()、rstrip()
2. 删除丹哥固定位置的字符，可以使用切片+拼接的方式
3. 字符串的replace()或者re.sub()
3. 字符串translate()方法，可以同时删除多种不同字符
"""

"""
In [1]: s = '  abc  232  '

In [2]: s.strip()
Out[2]: 'abc  232'

In [3]: s.rstrip()
Out[3]: '  abc  232'

In [4]: s.lstrip()
Out[4]: 'abc  232  '

In [5]: s2 = '---abc+++'

In [6]: s2.strip('-+')
Out[6]: 'abc'

"""

"""
这个挺重要的

In [1]: import string

In [2]: str.translate?
Docstring:
S.translate(table) -> str

Return a copy of the string S in which each character has been mapped
through the given translation table. The table must implement
lookup/indexing via __getitem__, for instance a dictionary or list,
mapping Unicode ordinals to Unicode ordinals, strings, or None. If
this operation raises LookupError, the character is left untouched.
Characters mapped to None are deleted.
Type:      method_descriptor

# 制作翻译表
In [5]: bytes_tatrans = bytes.maketrans(b'abcdef', b'ABCDEF')

# 转换为大写，并删除字母
In [6]: print(b'abcdefooo'.translate(bytes_tatrans, b'o'))
b'ABCDEF'
"""