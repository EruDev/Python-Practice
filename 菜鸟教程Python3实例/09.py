# 以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：

n = int(input('请输入一个数字:'))

if n == 0:
	print('这个数是0')
elif n < 0:
	print('这个数是负数')
elif n > 0:
	print('这个数是正数')