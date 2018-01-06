# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,
# 特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。


def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

def print_fibo(scope):
	for i in range(scope):
		print('%d,' % fibo(i), end='')

if __name__ == '__main__':
	while True:
		number = int(input('\n请输入需要输出的斐波那契数列的项数:'))
		print_fibo(number)
