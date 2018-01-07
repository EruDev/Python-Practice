#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

L2 = []
for x in range(1, 1001):
	L1 = []
	for i in range(1, int(x/2)+1):
		if x%i == 0:
			L1.append(i)
	if x == sum(L1):
		print(x)
		print(L1)
		L2.append(x)
		print('共有%d个完数' % len(L2))