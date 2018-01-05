# 如何判断字符串a是否以字符串b开头或结尾？

"""
案例:
某文件系统目录下有一系列文件:
quicksort.c
graph.py
heap.java
install.sh
stack.cpp

编写程序给其中所有.sh文件和.py文件加上用户可执行权限

解决方法:
使用字符串的str.startswith()和str.endswith()方法
注意：多个匹配时参数使用元组

先在指定文件夹下创建好相应的文件

import os,stat # star判断文件的权限

os.listdir('.') # 列出当前路径下的所有文件

'判断以.py或者.sh结尾的文件'
[name for name in os.listdir('.') if name.endswith(('.py', '.sh'))] # 这里面只能用元组来接收，列表会报错的
"""