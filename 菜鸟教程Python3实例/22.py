# Python 最大公约数算法

n1 = int(input('请输入第一个数：'))
n2 = int(input('请输入第二个数：'))
hcf = 0

if n1 > n2:
	smaller = n2
else:
	smaller = n1

for i in range(1, smaller+1):
	if (n1%i) == 0 and (n2%i) == 0:
		hcf = i

print('%d,%d的最大公约数是:%d' % (n1,n2,hcf))
