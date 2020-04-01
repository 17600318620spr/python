'''
这是一个非常简单的游戏。这里有 21 根棍子，首先用户选 1 到 4 根棍子，然后电脑选 1 到 4 根棍子。
谁选到最后一根棍子谁就输。判断一下用户有赢的机会吗？如果没有的话，如何修改游戏规则可以使用户有赢的机会呢？
特别说明：用户和电脑一次选的棍子总数只能是5。
'''
#!/usr/bin/env python3
sticks = 21

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")

while True:
    print("Sticks left: " , sticks)
    if sticks == 1:
        print("You took the last stick, you loose")
        break
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took: " , (5 - sticks_taken) , "\n")
    sticks -= 5
