# 题目：使用lambda来创建匿名函数。

MAXNUM = lambda x,y: (x > y) * x + (x < y) * y
MINNUM = lambda x,y: (x < y) * x + (x > y) * y

print(MAXNUM(10 ,20)) 
print(MINNUM(10 ,20))

# 菜鸟教程上的例子是上面那个，个人感觉应该是等价下面这个的
def maxNum(x, y):
	if x > y:
		return x
	elif x < y:
		return y