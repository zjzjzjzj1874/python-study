#/usr/bin/python3

if __name__ == '__main__':
    age = int(input("请输入你们家狗狗年龄: "))
    print("")
    
    if age <= 0:
        print("你逗我玩呢！")
    elif age == 1:
        print("相当于人类14岁!")
    elif age == 2:
        print("相当于人类22岁!")
    else:
        human_age = 22 + (age - 2) * 5
        print("相当于人类{}岁!".format(human_age))
        
    ''' 退出提示 '''
    input("点击 enter 键退出")