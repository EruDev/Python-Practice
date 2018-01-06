# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def prime(num):
	L = []

	while num > 1:
		for i in range(2, num+1):
			if num % i == 0:
				num = int(num / i)
				L.append(i)
				break

	return L

n = input('输入一个正整数:')

if n.isdigit() and int(n) > 0:
	print(n, '=', '*'.join([str(x) for x in prime(int(n))]))
else:
	print('输入有误')

