# 猜数字小游戏

from random import randint
from collections import deque

history = deque([], 5) # 生成一个能存5个数字的双向队列
key = randint(0,100)

def guess(number):
	if number > key:
		print('%d is greater than key' % number)
	elif number < key:
		print('%d is less than key' % number)
	elif number == key:
		print('666,你猜对了')
		return True


while True:
	num = input('please input your number:')
	if num.isdigit(): # 判断输入的内容是否为数字
		k = int(num)
		history.append(k)  # 接收输入的num
		if guess(k):
			break
	elif num == 'history' or num == 'h?': # 如果输入的是history或者h? 则以列表的形式显示history中的内容
		print(list(history))

"""
OUT
please input your number:50
50 is less than key
please input your number:30
30 is less than key
please input your number:20
20 is less than key
please input your number:hh?
please input your number:h?
[50, 30, 20]
please input your number:11
11 is less than key
please input your number:22
22 is less than key
please input your number:32
32 is less than key
please input your number:h?
[30, 20, 11, 22, 32]
please input your number:29
29 is less than key
please input your number:h?
[20, 11, 22, 32, 29]
please input your number:
""“