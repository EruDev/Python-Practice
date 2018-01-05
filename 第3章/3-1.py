# 如何拆分含有多种分隔符的字符串？

"""
案例:
我们要把某个字符串依据分隔符号拆分不同的字段，
该字符串包含多种不同的分隔符，例如：
s = 'ab;cd,ef|jh\tigk\nlmn'

解决方法:
一、连续使用str.split()方法，每次处理一种分隔符
二、使用正则表达式re.split()方法，一次性拆分字符串 ---推荐
"""

"""
In [1]: s = 'ab;cd,ef|jh\tigk\nlmn'
   ...:

In [2]: import re

In [4]: re.split(r'[;,|\t\n]+', s)
Out[4]: ['ab', 'cd', 'ef', 'jh', 'igk', 'lmn']
"""