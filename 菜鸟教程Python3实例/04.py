# 以下实例为通过用户输入数字，并计算二次方程：

"""
二次方程a**x + bx + c
a、b、c由用户提供
"""
import cmath

a = float(input('请输入a:'))
b = float(input('请输入b:'))
c = float(input('请输入c:'))

d = (b**2) - (4*a*C)

s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为{}和{}'.format(s1, s2))