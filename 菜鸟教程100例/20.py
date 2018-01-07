# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？

tour = []
height = []

hei = 100.0
time = 10

for i in range(1, time+1):
	hei /= 2
	height.append(hei)

print('第10次反弹高度:height = {}'.format(height[-1]))