# Python 获取昨天日期

# 导入datetime模块
import datetime

def get_yesterday():
	today = datetime.date.today()
	oneday = datetime.timedelta(days=1)
	yesterday = today - oneday
	return yesterday

print(get_yesterday())