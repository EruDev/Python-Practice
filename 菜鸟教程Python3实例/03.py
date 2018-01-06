# 平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。

#以下实例为通过用户输入一个数字，并计算这个数字的平方根：

n = float(input('请输入一个数字:'))
n2 = n ** 0.5
print('%0.3f的平方根是:%0.3f' % (n,n2))

# 以上适用于正数，负数和复数可以用以下的方式:

import cmath

num = int(input('请输入一个数字:'))
num_sqrt = cmath.sqrt(num)
print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))