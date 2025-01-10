'''
Author: zjzjzjzj1874 zjzjzjzj1874@gmail.com
Date: 2025-01-09 17:19:57
LastEditors: zjzjzjzj1874 zjzjzjzj1874@gmail.com
LastEditTime: 2025-01-10 14:20:16
FilePath: /python-study/examples/calss.py
Description: class example
'''

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 运算符重载
    def __add__(self, other):
        return self.x + self.y + other.x + other.y
    # 
    def __sub__(self, other):
        return self.x + self.y - (other.x + other.y)

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        if self.y == 0:
            return "Error: division by zero"
        else:    
            return self.x / self.y    
        
    # 普通方法，需要实例化才能调用
    def hello(self):
        # python的类成员变量可以不在前面预先定义，在运行时自动创建
        self.z = 10
        print("hello world", self.z)
        
    # 静态方法, 无需实例化即可调用 MyClass.f1()
    @staticmethod
    def f1():
        print("f1")
    
    # 类方法, 无需实例化即可调用 MyClass.f2()
    @classmethod    
    def f2(cls):
        print("f2")
        
    # 私有方法, 不能被外部调用
    def _private_method(self):
        print("private method")
        
        
if __name__ == '__main__':
    obj = MyClass(2, 3)
    obj2 = MyClass(4, 0)
    # print(obj.add())
    # print(obj.sub())
    
    MyClass.f1()
    MyClass.f2()
    print(obj + obj2)
    print(obj - obj2)
    
    obj.hello()
    obj._private_method()