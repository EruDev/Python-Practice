# 如何进行反向迭代？

"""
案例:实现一个连续浮点数发生器，根据给定的范围(start,end)和步进值(step)产生
一些连续的浮点数，如迭代FloatRange(3.0, 4.0, 0.2)可生产序列:

正向:3.0->3.2->3.4->3.6->3.8->4.0
反向:4.0->3.8->3.6->3.4->3.2->3.0
"""

class FloatRange:

	def __init__(self, start,end, step=0.1):
		self.start = start
		self.end = end
		self.step = step

	def __iter__(self):
		"""实现正向迭代"""
		t = self.start
		while t <= self.end:
			yield t
			t += self.step

	def __reversed__(self):
		"""实现反向迭代"""
		t = self.end
		while t > self.start:
			yield t
			t -= self.step

for x in FloatRange(1.0, 3.0, 0.5):
	print(x)

for x in reversed(FloatRange(1.0,3.0,0.5)):
	print(x)
"""
OUT
1.0
1.5
2.0
2.5
3.0

3.0
2.5
2.0
1.5
"""