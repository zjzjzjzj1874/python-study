'''
Author: zjzjzjzj1874 zjzjzjzj1874@gmail.com
Date: 2025-01-07 16:58:53
LastEditors: zjzjzjzj1874 zjzjzjzj1874@gmail.com
LastEditTime: 2025-01-07 17:34:59
FilePath: /python-study/examples/decorator.py
Description: 装饰器介绍
'''

# 装饰器函数，修改返回参数
def myDecorator(func):
    def wrapper():
        print("myDecorator")
        result = func()
        return result + " - 修改后的返回值"
    return wrapper

# 装饰器函数，修改参数
def myDecorator2(func):
    def wrapper(*args, **kwargs):
        print("myDecorator2")
        result = func(*args, **kwargs)
        return result + " - 修改后的返回值"
    return wrapper

# 装饰器函数，在函数执行前修改对应的参数
def before(*args, **kwargs):
    print(f"args == {args}")
    print(f"kwargs == {kwargs}")
    kwargs["name"] = "李四"
    print(f"kwargs == {kwargs}")
    return kwargs

def after(*args, **kwargs):
    print(f"args == {args}")
    print(f"kwargs == {kwargs}")
    kwargs["city"] = "成都"
    print(f"kwargs == {kwargs}")
    return kwargs

# args和kwargs的区别
# args是位置参数，kwargs是关键字参数
# 位置参数和关键字参数的区别
# 位置参数：按照位置顺序传递参数
# 关键字参数：按照参数名传递参数
def myDecorator3(func):
    def wrapper(*args, **kwargs):
        kwargs = before(*args, **kwargs)
        func(*args, **kwargs)
        kwargs = after(*args, **kwargs)
        return kwargs
    return wrapper

# 原始函数，不加参数
@myDecorator
def myFunc():
    a = "hello world"
    print(f"a == {a}")
    return a

# 原始函数，加参数
@myDecorator2
def myFunc2(a):
    print(f"a == {a}")
    return a

@myDecorator3
def myFunc3(name, age, city="Beijing"):
    print(f"name={name}, age={age}, city={city}")
    return f"Hello, {name}"

if __name__ == '__main__':
    # print(f"myFunc == {myFunc()}")
    
    # print(f"myFunc2 == {myFunc2("aaa")}")
    
    # 测试myDecorator3
    result = myFunc3(name="张三", age=25, city="上海")
    print(f"myFunc3 result: {result}")
    
    
    
    
