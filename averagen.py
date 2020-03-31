# 求N个数字的平均值 程序中将要输入10个数字，最后计算10个数字的平均值

#!/usr/bin/env python3
N=10
sum=0
count=0
print("please input 10 numbers:")

while count<N:
    number=float(input())
    sum=sum+number
    count=count+1
average=sum/N
print("N={}, sum={}".format(N, sum))
print("Average={:.2f}".format(average))
