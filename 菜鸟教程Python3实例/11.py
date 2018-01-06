# 以下实例用于判断一个数字是否为奇数或偶数：

n = int(input('请输入一个数字:'))

if n%2 == 0:
	print('{}是偶数'.format(n))
else:
	print('{}是奇数'.format(n))