# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

def test(num):

	length = len(num)
	print('%s的位数是:%s' % (num, length))
	
	for i in num[::-1]:
		print(i)


num = input('请输入一个不多于5位的正整数:')
test(num)