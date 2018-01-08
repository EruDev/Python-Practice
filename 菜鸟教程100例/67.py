
# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

li = [1, 2, 3, 7, 9, 8]  

for i in range(len(li)):
	if li[i] == max(li):
		li[0], li[i] = li[i], li[0]

for j in range(len(li)):
	if li[j] == min(li):
		li[len(li)-1], li[j] = li[j], li[len(li)- 1]

print(li)
