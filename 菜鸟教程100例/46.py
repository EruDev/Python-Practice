# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。

n = int(input('enter the num:'))
n2 = n**2

if n2 < 50:
	exit(0)