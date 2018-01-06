# Python ASCII码与字符相互转换

ch = input('请输入一个字符:')

n = int(input('请输入一个ASCII码:'))

print(ch + '的ASCII码', ord(ch))
print(n, '对应的字符为', chr(n))