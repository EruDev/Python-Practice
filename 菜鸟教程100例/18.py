# 题目：求s=a+aa+aaa+aaaa+aa...a的值，
# 其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

sum_nums = 0
nus = []

n = int(input('n = '))
num = int(input('num = '))

for each in range(n):
	sum_nums += num
	num = num * 10
	nus.append(sum_nums)
	print(sum_nums)
print('计算的和为:',sum(nus))