#-*-coding:utf-8-*-
#Python 核心编程 第六章
print '-' * 15
print '''
序列:
	标准类型操作符一般都能适用与所有的序列类型
	序列类型操作符号：
		seq[ind]
		seq[ind1:ind2]
		seq * expr	序列重复expr次
		seq1 + seq2 	
		obj in seq
		obj not in seq

	内建函数（BIFs）:
		类型转换；
			list()
			str()
			unicode()
			basestring()	note:仅仅作为str unicode函数提供父类 不能被实例化 也不能被调用
			tuple()
		Operational:
			enumerate(item)		返回一个enumerate对象 由index和item值组成的元组
			len()
			max()
			min()
			reversed()
			sorted()
			sum()
			zip()			返回每个元素组成的元组
'''

print '-' * 15
print '''
字符串：
	字符串类型是不可变的
	字符串是一种序列
	
	sring 模块的一些用法:
		string.ascii_uppercase 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		string.ascii_lowercase 'abcdefghijklmnopqistuvwxyz'
		string.ascii_letters 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		string.digits '0123456789'
	
	'+'操作符：
		可以用 字符串格式化 或者 join方法 代替
'''	

print '-' * 15
print '''
只适用于字符串的操作符：
	格式化操作符 % 

	字符串模板：
		from string import Template
		s = Template('There are ${howmany} ${lang} Quotation Symbols')
	
		print s.subsitute(lang = 'Python', howmany = 3)
		print s.safe_subsitute(lang = 'Python', howmany = 3)

	
	原始字符串操作符：
		r/R	在正则表达式中很有用 re
	
	Unicode字符串；
		u/U
'''

print '-' * 15
print '''
	字符串内建函数：
		实现了string模块的大部分功能，数量较多
'''


print '-' * 15
print '''
	列表：
		创建 [] list()
		更新	append() 
		删除 remove()	pop() del[]
'''

print '-' * 15
print '''

'''
