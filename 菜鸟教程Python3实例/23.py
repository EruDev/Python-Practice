# Python 最小公倍数算法

def lcm(x, y):
	# 获取最大的数
	if x > y:
		greater = x
	else:
		greater = y


	while True:
		if (greater%x) == 0 and (greater%y) == 0:
			mul = greater
			break
		greater += 1

	return mul

n1 = int(input('请输入第一个数：'))
n2 = int(input('请输入第二个数：'))
print('%d,%d之间的最小公倍数是:%d' % (n1, n2, lcm(n1, n2)))

