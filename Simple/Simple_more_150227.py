#-*-coding:utf-8-*-

#简明python教程 第15章 更多Python的内容

print '''
特殊的方法:
	__init__(self,...)	
	__del__()
	__str__() 在我们对对象使用print语句或是使用str()的时候调用
	__lt__(self,other) 当使用 小于 运算符的时候调用. 类似的，对于所有的运算符都有特殊的方法
	__getitem__(self, key) 使用x[key]索引操作符的时候调用
	__len__(self)	对序列对象使用内建的len()函数的时候调用
'''

print '01'
print '-' * 15

'''
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]

print listtwo
'''

print '''
列表综合
'''

print '02'
print '-' * 15


#def powersum(power, *args):
	#total = 0
	#for i in args:
		#total += pow(i, power)

	#return total

#print powersum(2, 3, 4)
#print powersum(3, 4)


print '''
在函数中接受元组和列表：
	当要使函数接受元组或字典形式的参数的时候，有一种特殊的方法，它分别使用*和**前缀，这种方法在函数需要获取可变数量的参数的时候特别有用
'''

print '03 lambda形式'
print '-' * 15


#def make_repeater(n):
	#return lambda s: s*n

#twice = make_repeater(2)

#print twice

#print twice('word')
#print twice(5)


print '''
lambda 语句用来创建函数对象**函数对象**
本质上 lambda需要一个参数，后面仅跟单个表达式作为函数体
'''

print '04 exec 和 eval 语句'
print '-' * 15

#exec 'print "Hello woeld"'
#print eval ('2*5')


print '''
exec 语句用来执行储存在字符串或文件中的Python语句
eval 语句用来计算存储在字符串中的有效的Python表达式
'''

print '05 assert语句'
print '-' * 15

#mylist = ['item']

#assert len(mylist) >= 1

#mylist.pop()

#assert len(mylist) >= 1

print '''
assert 语句用来声明某个条件是真的 如果仅仅是验证某个条件的真假，并非真的引发一个错误 assert是理想语句
assert 语句失败的时候会引发一个AssertionError
'''
print '06 repr函数'
print '-' * 15

#i = []
#i.append('item')

#print i
#j =  `i`
#print j

#h = repr(i)
#print h

print '''
repr 函数用来去得对象的规范字符串表示。反引号(也称转换符)也具有相同的功能
大部属时候有 eval(repr(object)) == object
类的__repr__方法可以控制对象在被repr函数调用时候返回的内容
'''

