# 如何为元组中的每个元素命名，提高可读性 二

"""
In [1]: from collections import namedtuple

In [2]: Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

In [3]: s = Student('zhangsan', '12', 'male', 'zhangsan@qq.com')

In [4]: s
Out[4]: Student(name='zhangsan', age='12', sex='male', email='zhangsan@qq.com')

In [5]: s.name
Out[5]: 'zhangsan'

In [6]: s.age
Out[6]: '12'

In [7]: s.sex
Out[7]: 'male'

In [8]: s.email
Out[8]: 'zhangsan@qq.com'

In [9]: isinstance(s, tuple) # 判断类型
Out[9]: True

"""