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
