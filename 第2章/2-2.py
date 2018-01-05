# 如何使用生成器函数实现可迭代对象？

"""
案例:实现一个可迭代对象的类，它能迭代出给定范围内的所有素数

pn=PrimeNumbers(1,30)
for n in pn:
	print(n)
输出结果:2 3 5 7 11 13 17 19 23 29

解决方法:将该类的__iter__方法实现生成器函数，每次yield返回一个素数
"""

# def f():
# 	print('in f() 1')
# 	yield 1
# 	print('in f() 2')
# 	yield 2
# 	print('in f() 3')
# 	yield 3
	
# g = f()
# print(next(g))
# print(next(g))
# print(next(g))
# for i in g:
# 	print(i)

class PrimeNumbers:

	def __init__(self, start, end):
		self.start = start
		self.end = end

	def isPrime(self, k):
		if k < 2:
			return False

		for i in range(2, k):
			if k % 2 == 0:
				return False
			return True

		return True

	def __iter__(self):
		for k in range(self.start, self.end + 1):
			if self.isPrime(k):
				yield k

for i in PrimeNumbers(1,20):
	print(i)
