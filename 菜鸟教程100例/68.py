# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

li = [1, 2, 3, 4, 5, 6] # 测试列表
m = 3                   # 设置向后移动3位

for _ in range(m):
	li.insert(0, li.pop())


print(li)