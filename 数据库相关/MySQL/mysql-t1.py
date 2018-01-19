#coding=utf-8

import MySQLdb

try:
	
	# 连接数据库
	conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='python3', charset='utf8')
	# 操作游标
	cursor = conn.cursor()
	user_name = input('请输入用户名:')
	# sql语句
	# sql = 'insert into students(name) values("老王")'
	# sql = 'update students set name="小王" where id=11'
	# sql = 'delete from students where id=11'
	sql = 'insert into students(name) values(%s)'
	# 执行sql语句
	cursor.execute(sql, [user_name])
	conn.commit()
	cursor.close()
	conn.close()
	print('ok')
except Exception as e:
	print(e)