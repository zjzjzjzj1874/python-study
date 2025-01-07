'''
Author: zjzjzjzj1874 zjzjzjzj1874@gmail.com
Date: 2024-12-31 15:43:57
LastEditors: zjzjzjzj1874 zjzjzjzj1874@gmail.com
LastEditTime: 2024-12-31 15:45:24
FilePath: /python-study/examples/guess_numberpy
Description: guess_number.py
'''
#/usr/bin/Python3

if __name__ == '__main__':
    '''猜字谜'''
    number = 42
    guess = -1
    
    print("数字猜谜游戏开始！")
    
    while guess != number:
        guess = int(input("请输入你猜的数字(0-100之间)："))
        if guess == number:
            print("恭喜你，猜对了！")
        elif guess < number:    
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")
    
    print("游戏结束！")