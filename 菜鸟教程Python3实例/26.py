# 以下代码演示了Python基本的文件操作，包括 open，read，write：

with open('test.txt', 'w', encoding='utf-8') as f:
	f.write('你好啊')

with open('test.txt', 'r', encoding='utf-8') as f:
	print(f.read())