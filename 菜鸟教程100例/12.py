# 题目：判断101-200之间有多少个素数，并输出所有素数。


for num in range(101, 200):
	for i in range(2, num):
		if (num % i) == 0:
			break
	else:
		print(num)