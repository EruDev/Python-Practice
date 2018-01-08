# 题目：打印出杨辉三角形（要求打印出10行如下图）。　

def triangles():
	a = [1]
	while True:
		yield a
		a = [sum(i) for i in zip([0] + a, a+ [0])]

if __name__ == '__main__':
	n = int(input('请输入您想要显示的最大行数:'))
	tri = triangles()
	for i in range(n):
		print(next(tri))