<!--
 * @Author: zjzjzjzj1874 zjzjzjzj1874@gmail.com
 * @Date: 2024-12-16 14:42:38
 * @LastEditors: zjzjzjzj1874 zjzjzjzj1874@gmail.com
 * @LastEditTime: 2024-12-31 15:01:28
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




