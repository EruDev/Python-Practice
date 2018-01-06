# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

# n1 = int(input('请输入第一个整数:'))
# n2 = int(input('请输入第二个整数:'))
# n3 = int(input('请输入第三个整数:'))

# nums = []
# nums.append(n1)
# nums.append(n2)
# nums.append(n3)
# print(sorted(nums))
nums = []
for i in range(3):
	num = int(input('输入一个整数:'))
	nums.append(num)

print(sorted(nums))
