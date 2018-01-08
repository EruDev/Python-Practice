# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

weekDict = {'M':'Monday', 'T':{'u': 'Tuesday', 'h':'Thursday'}, 'W':'Wednesday', 'F':'Friday', 
	'S':{'a':'Saturday', 'u':'Sunday'}}

day = input('输入第一个字母：')
day = day.upper()

if day in ['T', 'S']:
	day2 = input('输入第二个字母：')
	print(weekDict[day][day2])
else:
	print(weekDict[day])