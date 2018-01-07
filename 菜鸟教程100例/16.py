# 题目：输出指定格式的日期。

import time

local = time.localtime(time.time())
str_local = time.strftime('%Y-%m-%d-%H:%M:%S', local)
print(str_local)