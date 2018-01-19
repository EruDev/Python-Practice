#coding=utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1

name = input('请输入用户名:')
pwd = input('请输入密码:')

s1 = sha1()
s1.update(pwd)
pwd2 = s1.hexdigest()

sql = 'select upwd from userinfos where uname=%s'
helper = MysqlHelper('localhost',3306,'root','root','python3')
result = helper.search_all(sql,[name])

if len(result) == 0:
	print('用户名错误')
elif result[0][0] == pwd2:
	print('登录成功')
else:
	print('密码错误')