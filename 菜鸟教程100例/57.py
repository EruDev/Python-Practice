# 题目：画图，学用line画直线。

import turtle

def drawLine(n):
	t = turtle.Pen()
	t.color(0.3, 0.8, 0.6) # 设置颜色
	t.begin_fill()
	for i in range(n):
		t.forward(50)
		t.left(360/n)
	t.end_fill()

drawLine(4)