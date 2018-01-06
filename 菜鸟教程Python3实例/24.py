# Python 简单计算器实现

# 定义函数
def add(x, y):
	"""相加"""
	return x + y

def subtract(x, y):
	"""相减"""
	return x - y

def multiply(x, y):
	"""相乘"""
	return x * y

def divide(x, y):
	"""相除"""
	return x / y
while True:
	n1 = int(input('请输入第一个数:'))
	n2 = int(input('请输入第二个数:'))
	choice = input('请输入你的选择(1)-相加，(2)-相减, (3)-相乘, (4)-相除:')

	# 判断
	if choice == '1':
		print('%d, %d相加是:%d' % (n1, n2, add(n1,n2)))
	elif choice == '2':
		print('%d, %d相减是:%d' % (n1, n2, subtract(n1,n2)))
	elif choice == '3':
		print('%d, %d相乘是:%d' % (n1, n2, multiply(n1,n2)))
	elif choice == '4':
		print('%d, %d相除是:%d' % (n1, n2, divide(n1,n2)))
	else:
		print('非法输入')