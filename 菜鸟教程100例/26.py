# 题目：利用递归方法求5!。

def fact(n):
	if n == 1 or n == 0:
		return 1
	else:
		return fact(n-1)*n

print(fact(5))