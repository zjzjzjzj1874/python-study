'''
Author: zjzjzjzj1874 zjzjzjzj1874@gmail.com
Date: 2024-12-16 18:28:41
LastEditors: zjzjzjzj1874 zjzjzjzj1874@gmail.com
LastEditTime: 2025-01-07 16:54:21
FilePath: /python-study/examples/data_type.py
Description: python的数据类型
'''

import math # 导入math模块，用于计算

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
    
    # 其他输出的方法
    # 使用str.format()方法
    print("Hello, {0}, 成绩提升了 {1:.2f}%".format("小明", 10.56789))
    # 使用f-string
    name = "小明"
    score = 10.56789
    print(f"Hello, {name}, 成绩提升了 {score:.2f}%")    
    
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

def dict_test():
    print("----------------- dict_test -----------------")
    # 字典类型，键值对的集合，键必须是不可变类型，如字符串、数字、元组等
    # 字典是无序的，键值对的集合，键必须是不可变类型，如字符串、数字、元组等
    # 字典的键必须是唯一的，不能重复，值可以重复
    # 字典的键值对通过冒号分隔，键和值用逗号分隔
    # 字典的创建方式有两种，第一种是通过{}，第二种是通过dict()方法
    # 字典的访问方式和列表类似，通过键访问值
    # 字典的修改方式和列表类似，通过键修改值
    # 字典的删除方式和列表类似，通过del语句删除键值对
    # 字典的长度通过len()方法获取   
    
    a = {'name': '小明', 'age': 18, 'gender': '男', 1: 'one'} # 字典,key类型可以是数字、字符串、元组等
    print("a == ",a)
    print("a['name'] == ",a['name'])
    a['age'] = 19 # 修改值
    print("a['age'] == ",a['age'])
    a['city'] = '北京' # 添加键值对
    print("a['city'] == ",a['city'])
    del a['city'] # 删除键值对
    print("a == ",a)
    print("len(a) == ",len(a))
    
    # 字典的遍历方式    
    for key in a:
        print(key, a[key])
    
    print(" ---------- map range with key value ---------")
    for key, value in a.items():
        print(key, value)
    
    print(" ---------- map a.fromkeys() ---------")
    nd = dict.fromkeys(a) # 通过fromkeys()方法创建字典
    print("nd == ",nd)
    
    # 字典的更新方式
    a.update({'name': '小明变小红', 'age': 20})
    print("a == ",a)
    
    # 字典的合并方式
    b = {'name': '小张', 'age': 21}
    a.update(b)
    print("a == ",a)
    
    # 字典的删除方式
    del a['age']
    print("a == ",a)
    
    # 字典的清空方式
    a.clear()
    print("a == ",a)
    
    # 字典的拷贝方式
    c = a.copy()
    print("c == ",c)
    
    # 字典的键值对排序方式
    d = {'name': '小明', 'age': 18, 'gender': '男'}
    print("d == ",d)
    # 按键排序
    for key in sorted(d):
        print(key, d[key])
    
def num_test():
    ''' 数字类型 '''
    print("----------------- num_test -----------------")
    
    print(math.sin(math.radians(30))) # 转成弧度
    
    print(abs(-10))# 绝对值
    
def lambda_test():
    print("----------------- lambda_test -----------------")
    # 闭包，闭包是函数内部的函数，可以访问函数内部的变量
    def mf(n):
        return lambda x: x * n
    
    mf1 = mf(1)
    mf2 = mf(2)
    mf3 = mf(3)
    print(mf1(10))
    print(mf2(10))
    print(mf3(10))
    
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
    # set_test()
    
    # 字典类型    
    # dict_test()
    
    # 数字类型
    # num_test()
    
    # 闭包
    lambda_test()
    
    
    
    
    

