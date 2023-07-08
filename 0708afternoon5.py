#!/usr/bin/python 3.10.2

import random

def playGame():
    min = 1
    max = 10
    count = 0
    target = random.randint(min, max)
    print("=======猜數字遊戲=======\n\n")

    while True:
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin == target):
            print(f"Bingo!猜對了, 答案是:{target}")
            print(f"您共猜了{count}次")
            break
        else:
            print("猜錯了")
            print(f"您已經猜了幾{count}次")

while(True):
    playGame()
    play_again = input("還要玩嗎? (y,n)")
    if not (play_again == 'y'):
        break
print("遊戲結束")

