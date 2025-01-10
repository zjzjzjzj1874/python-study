<!--
 * @Author: zjzjzjzj1874 zjzjzjzj1874@gmail.com
 * @Date: 2024-12-16 14:42:38
 * @LastEditors: zjzjzjzj1874 zjzjzjzj1874@gmail.com
 * @LastEditTime: 2025-01-10 14:40:59
 * @FilePath: /python-study/README.md
 * @Description: python学习笔记
-->

# python-study
Python Study

## python简介
Python是解释性、编译型、互动型的面向对象的脚本语言。
* 解释型语言：开发过程中没有编译环境，类似PHP和Perl；
* 交互式语言：在Python>>>后可直接执行代码；
* 面向对象：支持面向对象的风格或代码封装；
* 初学者友好：从简单的文字处理到web应用，再到游戏、算法开发都支持。

### 发展历史
* 20世纪80年代末、90年代初，由Guido van Rossum在荷兰国家数学和计算机科学研究所设计出来的；
* 像Perl一样，Python源代码遵守GPL(GNU General Public License)协议；
* Python2.0于2000年10月16日发布，增加GC，支持Unicode；
* Python3.0于2008年12月3日发布，此版本不完全兼容之前的源码；
* Python2.7是Python2.x的最后版本，支持了部分Python3.1的语法；

### 特点
* 易于学习：关键字少，结构简单；
* 易于阅读：代码定义比较清晰；
* 易于维护：源代码相当容易维护；
* 广泛的标准库：丰富的库，跨平台，在Unix、Windows和MacOS兼容很好；
* 互动模式：从终端输入执行代码，互动测试和调试代码片段；
* 可移植：基于其开放源码特性，被移植到很多平台了；
* 可扩展：如果有一段运行很快，或者不想开放的算法，可以使用C/C++完成，然后在Python中调用；
* 数据库：提供所有主要的商业数据库接口；
* GUI编程：Python支持GUI可以创建和移植许多系统调用；
* 可嵌入：可以将Python嵌入到C/C++程序，让程序用户获得脚本化能力；

### 应用
* YouTube
* Reddit-社交分享
* Dropbox-文件分享
* 豆瓣
* 知乎
* 果壳
* bottle
* EVE-网络游戏EVE大量使用Python开发
* Bleander-使用Python作为建模工具


## 基础语法

### 引入包

* 导入整个包/模块：`import time`
```python
import time
print(time.time())
```
* 导入模块中某个函数：`from time import sleep`
```python
from time import time
print(time())
```
* 导入多个函数：`from time import sleep, time`
```python
from time import sleep, time
sleep(1)
print(time())
```
* 导入全部函数：`from time import *`
> 和上面调用方法一致

## 基础数据类型

### 字符串类型

* 单引号和双引号都可以表示字符串，但建议使用单引号
```python
s1 = 'hello'
s2 = "world"
```
* 字符串可以用加号拼接
```python
s3 = s1 + s2
print(s3)
```
* 字符串可以用乘号重复
```python
s4 = s1 * 3
print(s4)
```
* 字符串可以用索引访问单个字符
```python
```

### dict字典类型

* dict.fromkeys() 
> 这个方法作用是生成一个新的dict字典；传参第一个是可迭代的，作为生成的key，第二个是value，作为其dict的默认值，不传的话默认值是None。


## python 运算符

### 算术运算符 
* `+ - * /` ：加减乘除
* `//` ：取整数，小的方向取
* `%` ：取模
* `**`：幂运算 eg：2**3=8 => 2^3 = 8

### 比较运算符
* `==` 、 `!=` 、 `<` 、 `>` 、 `<=` 、 `>=` ：等于、不等于、小于、大于、小于等于、大于等于

### 赋值运算符
* `=` ：赋值
* `+=` 、 `-=` 、 `*=` 、 `/=` 、 `//=` 、 `%=` 、 `**=` ：加等于、减等于、乘等于、除等于、取整数等于、取模等于、幂等于
* `:=` 海象运算符(python3.8新增)：将右边的值赋值给左边的变量，右边的值可以是表达式。

```python 
# 传统写法
a = 10
if a > 5:
    print(a)
    
# 新写法
if (a := 10) > 5:
    print(a)
```

### 位运算符
* `&` 、 `|` 、 `^` 、 `~` 、 `<<` 、 `>>` ：与、或、异或、取反、左移、右移

### 逻辑运算符
* `and` 、 `or` 、 `not` ：与、或、非
```python
a = 10
b = 20
c = 30
if (a > 5 and b < 15):
    print(a)
if (a > 5 or b < 15):
    print(b)
if (not c > 25):
    print(c)
```

### 成员运算符
* `in` 、 `not in` ：是否在序列中、是否不在序列中
```python
s = [1, 2, 3, 4, 5]
if 3 in s:
    print(True)
if 6 not in s:
    print(True)
```

### 身份运算符
* `is` 、 `is not` ：是否是同一个对象、是否不是同一个对象
```python
a = 10
b = 10
if a is b:
    print(True)
if a is not b:
    print(True)
```


## 面向对象编程

### 类  
* 定义类：`class 类名(object):`
* 实例化对象：`对象名 = 类名()`
* 访问属性：`对象名.属性名` 

* 类的方法
    * 普通方法：对象访问，实例化之后才能访问
    * 私有方法：两下划线开头，只能在内部访问
    * 静态方法：类和对象访问，不能和其他方法重名，否则会相互覆盖，后面定义覆盖前面
    * 类方法：类和对象访问，第一个参数是类，而不是实例化的对象，后面定义覆盖前面
类的专有方法：
* `__init__` : 构造函数，在生成对象时调用
* `__del__` : 析构函数，释放对象时使用
* `__repr__` : 打印，转换
* `__setitem__` : 按照索引赋值
* `__getitem__`: 按照索引获取值
* `__len__`: 获得长度
* `__cmp__`: 比较运算
* `__call__`: 函数调用
* `__add__`: 加运算
* `__sub__`: 减运算
* `__mul__`: 乘运算
* `__truediv__`: 除运算
* `__mod__`: 求余运算
* `__pow__`: 乘方
* `__divmod__`: 除法运算
* `__floordiv__`: 整除运算
* `__radd__`: 右加运算
* `__rsub__`: 右减运算
* `__rmul__`: 右乘运算
* `__rtruediv__`: 右除运算
* `__rpow__`: 右乘方


## 标准库预览

### os模块
* os.path.abspath(path) ：返回path规范化的绝对路径
* os.path.split(path) ：将path分割成目录和文件名二元组返回
* os.path.dirname(path) ：返回path的目录。其实就是os.path.split(path)的第一个元素
* os.path.basename(path) ：返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
* os.path.exists(path) ：如果path存在，返回True；如果path不存在，返回False
* os.path.isabs(path) ：如果path是绝对路径，返回True
* os.path.isfile(path) ：如果path是一个存在的文件，返回True。否则返回False
* os.path.isdir(path) ：如果path是一个存在的目录，则返回True。否则返回False
* os.path.join(path1[, path2[, ...]]) ：将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
* os.path.getsize(path) ：返回path的大小
* os.getcwd() ：返回当前工作目录
* os.chdir(path) ：改变当前工作目录
* os.listdir(path) ：返回path指定的文件夹包含的文件或文件夹的名字的列表
* os.mkdir(path) ：创建path路径
* os.rmdir(path) ：删除path路径
* os.remove(path) ：删除path路径
* os.rename(old, new) ：重命名文件或目录，从old到new

### sys模块
* sys.argv ：命令行参数List，第一个元素是程序本身路径
* sys.exit(n) ：退出程序，正常退出时exit(0)
* sys.version ：获取Python解释程序的版本信息
* sys.path ：返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
* sys.platform ：返回操作系统平台名称

命令行参数
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
```python
>> import sys
>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

### time模块
* time.time() ：返回当前时间戳
* time.sleep(seconds) ：暂停seconds秒
* time.strftime(format[, t]) ：返回格式化的时间
* time.strptime(string[, format]) ：把一个格式化时间字符串转化为struct_time
* time.mktime(t) ：把一个struct_time转化为时间戳

### datetime模块
* datetime.datetime.now() ：返回当前日期和时间
* datetime.datetime.strptime(date_string, format) ：把一个格式化时间字符串转化为datetime对象
* datetime.datetime.strftime(datetime_object, format) ：把一个datetime对象转化为格式化时间字符串

### random模块
* random.random() ：返回0到1之间的随机浮点数
* random.randint(a, b) ：返回a到b之间的随机整数
* random.choice(sequence) ：从序列中随机选择一个元素
* random.shuffle(sequence) ：将序列中的元素随机排序
* random.sample(sequence, k) ：从序列中随机选择k个元素

### math模块

### 正则模块

### json模块  

### urllib模块
