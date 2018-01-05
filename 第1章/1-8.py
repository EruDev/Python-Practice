# sample(seq, n) 从序列seq中选择n个随机且独立的元素；

"""

In [3]: from random import randint, sample

In [4]: sample('abcdefg', 3)
Out[4]: ['f', 'g', 'b']

In [5]: sample('abcdefg', randint(3,6))
Out[5]: ['a', 'b', 'c', 'e', 'd']

In [6]: s1 = {x: randint(1,4)for x in sample('abcdefg', randint(3,6))}

In [7]: s1
Out[7]: {'b': 4, 'c': 3, 'd': 2, 'e': 2, 'f': 2, 'g': 4}

In [8]: s2 = {x: randint(1,4)for x in sample('abcdefg', randint(3,6))}

In [9]: s3 = {x: randint(1,4)for x in sample('abcdefg', randint(3,6))}
"""