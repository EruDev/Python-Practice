# 以下实例为通过用户输入三角形三边长度，并计算三角形的面积：

# abc为三角形三条边


a = float(input('请输入a:'))
b = float(input('请输入b:'))
c = float(input('请输入c:'))

p = (a + b + c) / 2
s = (p*(p-a)*(p-b)*(p-c)) ** 0.5

print('已知三角形的三条边{0}、{1}、{2}、面积为:{3:0.2f}'.format(a, b, c, s))