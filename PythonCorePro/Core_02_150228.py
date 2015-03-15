#-*-coding:utf-8-*-

# Python 核心编程 第二章Chapter

print '语句和表达式的区别是 表达式没有关键字'

print '''
下划线 (_) 在解释器中有特别的含义，表示最后一个表达式的值
'''
print '''
输出重定向符号 (>>) 

sys.stderr	代表标准错误输出
''' 

print '''
decimal 十进制的浮点数

并不算内置类型 需要导入 decimal模块
'''

print '''
列表和元组可以存储不同类型的对象

元组与字符串一样 是不可改变的

列表可以改变 是有序的 可以添加 删除 的
'''

print '''
for 循环中同时循环索引和元素 的函数 enumerate()

for i, elem in enumerate(object):
	print elem, '%d' % i
'''

print '''
列表解析

squared = [x ** 2 for x in range(4)]

squared = [x ** 2 for x in range(8) if not x %2]
'''

print '''
Python 是通过引用调用的。这意味着函数内对参数的改变会影响到原始对象。\
不过只有可变对象才会受到影响，对不可变对象来说，它的行为类似按值调用
'''

print '''
moudle:
	sys 模块的三个用法:
				[ sys.stdout.write('')  sys.platform 平台 sys.version 版本 ]
'''
