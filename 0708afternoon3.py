#!/usr/bin/python 3.10.2

import random
min = 1
max = 100
count = 0
target = random.randint(min, max)
print("=======猜數字遊戲=======\n\n")
print(f"the answer is {target}")
while True:
    keyin = int(input(f"猜數字範圍{min}~{max}:"))
    count += 1
    if(keyin == target):
        print(f"Bingo！猜對了，答案是:{target}")
        print(f"您共猜了{count}次")
        break
    elif keyin > target:
        print("再小一點")
        max = keyin - 1
    elif keyin < target:
        print("再大一點")
        min = keyin + 1
    print(f"您已經猜了幾{count}次")
    if min == max:
        print(f"只剩下一個答案{max}")
        break
print("遊戲結束")
