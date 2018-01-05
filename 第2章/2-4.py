# 如何对迭代器做切片操作

"""
有某个文本文件，我们想读取其中某范围的内容，如100~300行之间的内容，
Python中文本文件是可迭代对象，我们是否可以用类似列表切片的方式
得到一个100~3--行文件内容的生成器？

f = opne('xxx.xxx')
f[100:300] 可以么?

解决方法:
可以使用标准库中的itertools.islice,它能返回一个迭代对象的切片生成器
"""

"""
利用itertools 下的 islice

In [4]: from itertools import islice

In [5]: islice?
Init signature: islice(self, /, *args, **kwargs)
Docstring:
islice(iterable, stop) --> islice object
islice(iterable, start, stop[, step]) --> islice object

Return an iterator whose next() method returns selected values from an
iterable.  If start is specified, will skip all preceding elements;
otherwise, start defaults to zero.  Step defaults to one.  If
specified as another value, step determines how many values are
skipped between successive calls.  Works like a slice() on a list
but returns an iterator.
Type:           type

In [6]: f = open('C:\\Users\\10279\\Desktop\\Python-Practice\\第2章\\poem.txt')

In [8]: for line in islice(f,100, 300):
   ...:     print(line)
   ...:

OUT

And he ran them single-handed till their sides were white with foam.

He followed like a bloodhound on their track,

Till they halted cowed and beaten, then he turned their heads for home,

And alone and unassisted brought them back.

But his hardy mountain pony he could scarcely raise a trot,

He was blood from hip to shoulder from the spur;

But his pluck was still undaunted, and his courage fiery hot,

For never yet was mountain horse a cur.
...
"""