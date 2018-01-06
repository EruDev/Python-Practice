# 题目：暂停一秒输出，并格式化当前时间。

import time

# print(time.localtime(time.time()))
while True:
	# 格式化输出当前时间
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
	# 暂停一秒
	time.sleep(1)