# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def palindrome(num):
	if num[::] == num[::-1]:
		print('%s是回文' % (num))
	else:
		print('不是回文')

num = input('输入一个5位数,thx:')
palindrome(num)