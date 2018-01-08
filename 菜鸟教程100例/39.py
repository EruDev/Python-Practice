# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

L = [1, 3, 15, 72, 99]

num = int(input('enter the num:'))

if num > L[len(L) - 1]:
	L.append(num)
elif num < L[0]:
	L.insert(0, num)
else:
	for i in range(len(L) - 1):
		if num > L[i] and num < L[i+1]:
			L.insert(i+1, num)
			break

print(L)
