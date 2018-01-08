# 题目：输入3个数a,b,c，按大小顺序输出.

li = []

for i in range(3):
	n = int(input('输入一个数:'))
	li.append(n)
li.sort()
print(li)