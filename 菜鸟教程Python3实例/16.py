# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。
# 即：n!=1×2×3×...×n。

def fact(n):

	if n < 1:
		return 1
	else:
		return n * fact(n - 1)

if __name__ == '__main__':
	print(fact(3))