#coding=utf-8

from MysqlHelper import MysqlHelper

# 修改
# name = input('请输入学生姓名：')
# n_id = input('请输入学生编号:')

# sql = 'update students set name=%s where id=%s'
# params = [name,n_id]

# sqlhelper = MysqlHelper('localhost',3306,'root','root','python3')
# sqlhelper.cud(sql,params)

# 查询

sql = 'select id,name from students where id<5'
sqlhelper = MysqlHelper('localhost',3306,'root','root','python3')
result = sqlhelper.search_all(sql)
print(result)