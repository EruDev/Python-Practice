 # 题目：对10个数进行排序。

L = []
N = 10

print('请输入十个数:\n')

for i in range(N):
 	L.append(int(input('请输入吧:\n')))

print()

for i in range(N):
 	print(L[i])

print()

# 排列数字
for i in range(N - 1):
	m = i
	for j in range(i+1, N):
		if L[m] > L[j]: m = j
	L[i], L[m] = L[m], L[i]
print('排列之后:')
for i in range(N):
	print(L[i])