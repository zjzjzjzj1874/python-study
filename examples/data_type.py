'''
Author: zjzjzjzj1874 zjzjzjzj1874@gmail.com
Date: 2024-12-16 18:28:41
LastEditors: zjzjzjzj1874 zjzjzjzj1874@gmail.com
LastEditTime: 2024-12-19 11:20:40
FilePath: /python-study/examples/data_type.py
Description: python的数据类型
'''
# 基础数据类型-字符串类型
def str_test():
    print("----------------- str_test -----------------")
    str = "hello world"
    print(str)
    print(len(str))
    print(str[0:-1]) # 打印第一个到倒数第二个字符，不包含最后一个
    print(str[2:5]) # 打印第三个到第五个字符，包含第五
    print(str[2:]) # 打印第三个到最后的字符
    print(str*2) # 打印字符串两次
    print(str+"!") # 连接字符串和字符
    
    # 转义特殊字符
    print('Hello\nWorld') # \n会被转义
    print(r'Hello\nWorld') # \n不会被转义
    
# 基础数据类型-布尔类型
def bool_test():
    print("----------------- bool_test -----------------")
    a = True
    print(type(a))
    print("0 == ", bool(0))
    print("1 == ", bool(1))
    print("100 == ",bool(100))
    print("[] == ",bool([]))
    print("[1,2,3] == ",bool([1,2,3]))
    print("python == ",bool('python'))
    print(" == ",bool(''))
    
# 基础数据类型-列表类型
def list_test():
    print("----------------- list_test -----------------")
    a = [1,2,3,4,5]
    print(a)
    
    b = [1,2,3,4,5, 'hello', 'world']
    print("before === ",b)
    # print(b*2) # 列表重复打印两次
    print("b[0] == ",b[0]) # 访问数组元素
    # 修改数组元素
    b[6] = 666
    print("after === ",b)
    # 追加元素
    b.append(777)
    print("after append === ",b)
    # print("b[7] == ",b[7]) # IndexError: list index out of range
    
# 元组和字符串一样，是不可修改的。
def tuple_test():
    print("----------------- tuple_test -----------------")
    a = (1,2,3,4,5)
    print("beofre === ",a)
    
    # a[0] = 111; # 报错 TypeError: 'tuple' object does not support item assignmen
    try:
        # 尝试修改元组元素，如果有异常将捕获异常
        a[0] = 111
    except TypeError as e:
        # 发生异常时，打印异常信息，如果不捕获异常，程序将终止
        print(e)
    finally:
        # finally, 无论异常是否发生都会执行
        print("after === ",a)

# 集合类型
def set_test():
    print("----------------- set_test -----------------")
    # 集合是无序的，不重复的元素的集合,这里要和列表区分开
    s = {1,2,3,4,5,1,'a','b'} # 创建集合
    print("s == ",s)
    s.add(6) # 添加元素
    print("s add 6 == ",s)
    s.remove(1) # 删除元素
    print("s remove 1 == ",s)
    s.update([7,8,9]) # 合并两个集合
    print("s update [7,8,9] == ",s)
    
    # set()。set方法创建的，其参数是需要可迭代的，如列表、元组、字符串等。数值类型不可迭代，所以不能作为参数传递
    b = set('abcd') # 另一种创建集合的方式
    a = set(s)
    c = set((1,2,3,4,5)) # 以元组作为参数创建集合
    print("a == ", a)
    print("b == ", b)
    print("c == ", c)
    print("a | b == ",a | b) # 并集
    print("a & b == ",a & b) # 交集
    print("a - b == ",a - b) # 差集
    print("a ^ b == ",a ^ b) # 对称差集，不同时存在的

# 反转字符串    
def reverseWords(input): 
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ") 
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
    # 重新组合字符串
    output = ' '.join(inputWords) 
    return output 

if __name__ == '__main__':
    # a = 10 # 整数
    # b = 3.14 # 浮点数
    # c = "hello world" # 字符串
    # d = True # 布尔值
    # e = None # 空值
    # print("abcde == ", a, b, c, d, e)
    
    # # 判断变量类型 => 这种即可实现类型判断
    # print("a == int? ",isinstance(a, int))
    # print("a == float? ",isinstance(a, float))
    
    # print("a name is ",type(a).__name__)
    
    # del a # 删除变量
    # print(a) # NameError: name 'a' is not defined
    
    # 字符串类型
    # str_test()
    
    # 布尔类型
    # bool_test()
    
    # 列表类型
    # list_test()
    
    # 字符串反转
    # input = 'I like hello world in python'
    # rw = reverseWords(input) 
    # print(rw)
    
    # 元组类型
    # tuple_test()
    
    # 集合类型
    set_test()
    
    

