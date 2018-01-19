# coding=utf-8

from MySQLdb import *

class MysqlHelper:

	def __init__(self,host,port,user,passwd,db,charset='utf8'):
		"""初始化"""
		self.host = host
		self.port = port
		self.user = user
		self.passwd = passwd
		self.db = db
		self.charset = charset

	def open(self):
		"""连接数据库"""
		self.conn = connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
		self.cursor = self.conn.cursor()

	def close(self):
		"""关闭连接"""
		self.cursor.close()
		self.conn.close()

	def cud(self,sql,parmas):
		"""执行sql语句"""
		try:
			self.open()

			self.cursor.execute(sql,parmas)
			self.conn.commit()

			self.close()

			print('ok')
		except Exception as e:
			print(e)

	def search_all(self,sql):
		"""查询所有数据"""
		try:
			self.open()

			self.cursor.execute(sql)
			result = self.cursor.fetchall()

			self.close()

			return result
		except Exception as e:
			print(e)
		