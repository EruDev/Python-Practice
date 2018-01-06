# 题目：输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('输入年份:'))
month = int(input('输入月份:'))
day = int(input('输入几号:'))

days = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

if month > 0 and month <= 12:
	sum_days = days[month - 1] + day

if (year % 4) == 0 and (year % 100 !=0) or (year % 400 == 0):
	if month > 2:
		leap = 1
		sum_days = days[month - 1] + day + leap

print('这一天是%d年的第%d天' % (year, sum_days))