#几个人轮流报数，凡遇到 7 的倍数，或含 7 的数字就要跳过，否则就算失败

for a in range(1,101):
    if a%7==0:
        continue
    elif a%10==7:
        continue
#    elif a // 10==7:
    elif int(a/10)==7:
        continue
    else:
        print(a)

