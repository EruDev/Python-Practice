# 以下实例用于判断用户输入的年份是否为闰年：

year = int(input('请输入一个数字:'))


if (year%4) == 0:
	if (year%100) == 0:
		if (year%400) == 0:
			print('{}是闰年'.format(year))
		else:
			print('{}不是闰年'.format(year))
	else:
		print('{}是闰年'.format(year))
else:
	print('{}不是闰年'.format(year))