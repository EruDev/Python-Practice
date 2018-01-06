# 题目：输出 9*9 乘法口诀表。

for i in range(1, 9):
	for j in range(1, i+1):
		print('{}×{}={}\t'.format(j, i, j*i), end='')
	print('')