# 题目：求1+2!+3!+...+20!的和。

s = 0
n = 0
t = 1

for n in range(1, 21):
	t = t * n
	s += t

print('1+2!+3!+...+20! = %d' % s)