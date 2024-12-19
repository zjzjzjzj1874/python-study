def main():
    # 条件语句
    print(r"------------------------------------------------------------")
    if True:
        print("True")
    else:
        print("False")

    # 循环语句
    print("Looping...")
    for i in range(10):
        print(i)

    # 多行语句
    print(r"------------------------------------------------------------")
    one = 1
    two = 2
    three = 3
    total = one + two + three
    print(one, " + ", two, " + ", three, " = ", total)
    
    if one == 1:
        print("one is equal to 1")
    elif one == 2:
        print("one is equal to 2")
    else:
        print("one is not equal to 1 or 2")

    # 字符串操作
    print(r"------------------------------------------------------------")
    str = "0123456789"
    print(str)  # 输出字符串
    print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
    print(str[0])  # 输出字符串第一个字符
    print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
    print(str[2:])  # 输出从第三个开始后的所有字符
    print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
    print(str[1:9:2])  # 输出从第二个开始到第10个且每隔一个的字符（步长为2）
    print(str * 2)  # 输出字符串两次
    print(str + "你好")  # 连接字符串
    print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

    print(r"------------------------------------------------------------")

import time
from time import time, sleep

# 确保代码仅在作为主程序运行时执行，不在被导入模块时执行。
if __name__ == "__main__":
    # main()
    # print(time.time())
    
    sleep(2) # 休眠2秒
    print(time())