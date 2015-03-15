#-*-coding:utf-8-*-
#Python 核心编程 第四章

print '-' * 15,
print '''
Python 对象

构造任何类型的值都是一个对象,Python中类型也是对象
对象的三个特性： 身份 类型 值

身份： 唯一的身份表示 id（）获得 该对象的内存地址
类型： type（）获得 
值：   数据
'''
print '-' * 15
print '''
标准类型:
	数字、整型、布尔型、长整型、浮点型、复数型、字符串、列表、元组、字典
'''

print '-' * 15
print '''
内建类型:
	类型、Null对象、文件、集合/固定集合、函数/方法、模块、类
	
类型本身也是对象

None对象的布尔值是False
'''
print '-' * 15
print '''
内部类型;
	代码对象、帧对象、跟踪记录对象、切片对象、省略对象、XRange对象

切片：
	步进切片 [:::]
	多维切片 [;,;] [...,;]

xrange() 用于需要节省内存使用或range()无法完成的超大数据集场合
'''

print '-' * 15
print '''
标准类型运算符:
	对象值的比较	> < >= <= == != 
	对象身份的比较 is 、is not
	布尔类型 not and or
'''

print '-' * 15
print '''
标准类型内建函数:
	cmp()	
	repr()
	str()
	type()
	isinstance()
'''

print '-' * 15
print '''
类型工厂函数：
	包括但不仅限于( int () float() list() tuple() dict())
'''

print '-' * 15
print '''
标准类型的分类：
	存储模型、更新模型、访问模型
	
	---------------------------------------------------------
	数据类型	存储模型	更新模型	访问模型
	数字		Scalar		不可		直接
	字符串		Scalar		不可		顺序
	列表		Container	可		顺序
	元组		Container	不可		顺序
	字典		Container	可		映射
	----------------------------------------------------------
'''

print '-' * 15
print '''
不支持的类型:
	char、byte、指针、int VS short VS long、 float VS double
'''
