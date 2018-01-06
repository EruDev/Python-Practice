# 题目：暂停一秒输出。

import time
from random import randint
d = {x:randint(1, 9) for x in range(10)}
print(d)
for k,v in d.items():
	print('%d:%d' % (k, v))
	time.sleep(1)
