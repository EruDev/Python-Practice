"""
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。

例如1^3 + 5^3 + 3^3 = 153。

1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""


lower = int(input('最小值:'))
upper = int(input('最大值:'))

for i in range(lower, upper+1):
	sum = 0
	# 指数
	n = len(str(i))

	temp = i
	while temp > 0:
		digit = temp % 10
		sum += digit ** n
		temp //= 10

	if i == sum:
		print(i)
	