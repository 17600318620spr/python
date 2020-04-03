'''
1.使用 open 打开文件 /tmp/String.txt 并读取其中的字符串
2.提取字符串中的所有数字，并组合成一个新的字符串，然后打印输出
提示：
    可以使用循环来访问字符串中的单个字符
    可以使用 isdigit() 来判断字符是否为数字
    使用 print() 把新的数字组成的字符串输出
'''
#!/usr/bin/env python3
# 打开并读取文件里的字符串
with open("/tmp/String.txt") as f:
    s=f.read()
res=''

# 循环字符串里的每个字符，判断是否为数字
for char in s:
    if char.isdigit():
        res+=char
print(res)
