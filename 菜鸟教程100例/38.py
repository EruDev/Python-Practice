# 题目：求一个3*3矩阵主对角线元素之和。

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum_ = 0

for i in range(3):
	sum_ += matrix[i][i]

print(sum_)