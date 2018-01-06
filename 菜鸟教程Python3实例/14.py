# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
# 换句话说就是该数除了1和它本身以外不再有其他的因数。

def is_prime(num):
	for i in range(2, num+1):
		if num%i == 0:
			return False
		return True

if __name__ == '__main__':
	num = int(input('请输入一个数字:'))
	print(num , is_prime(num))