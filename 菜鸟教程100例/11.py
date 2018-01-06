# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？

# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

def rabbits(month):
	
	if month == 1 or month == 2:
		return 1
	else:
		return rabbits(month-1) + rabbits(month - 2)

print(rabbits(5))

# def rabbit(num):
# 	 i = 1
# 	 a, b = 1, 1
# 	 while 1<=num:
# 	 	yield a
# 	 	i += 1
# 	 	a,b = b, a+b

# L1 = [x for x in rabbit(10)]
# print(L1)