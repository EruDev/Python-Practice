# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
from collections import Counter

s = input('请输入：')

print(Counter(s))
