# 题目：斐波那契数列。

def fibo(n):
	a, b = 1, 1
	for i in range(n-1):
		a,b = b, a+b
	return a

print(fibo(10))