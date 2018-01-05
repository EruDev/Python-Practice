# 如何为元组中的每个元素命名，提高可读性一

# ('Zhangsan', 15, 'male', 'zhangsan@qq.com')
# ('Lisi', 18, 'male', 'lisi@gmail.com')
# ('Wangwu', 12, 'female', 'wangwu@163.com')

NAME, AGE, SEX, EMAIL = range(4)

student = ('Zhangsan', 15, 'male', 'zhangsan@qq.com')

# name
print(student[NAME])
# age
if student[AGE] > 10:
	pass
# sex
if student[SEX] == 'male':
	pass
#...