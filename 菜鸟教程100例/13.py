# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# def is_daffodil(num):

# 	s = num // 100
# 	b = (num-100*s) // 10
# 	g = num - 100*s - b*10

# 	if (s**3) + (b**3) + (g**3) == num:
# 		return True
# 	else:
# 		return False

# print(is_daffodil(407))

for n in range(100, 1001):
	s = n // 100
	b = (n-100*s) // 10
	g = n - 100*s - b*10

	if (s**3) + (b**3) + (g**3) == n:
		print(n)
