#-*-coding:utf-8-*-
# 简明python教程 第十四章 Python标准库

print '01'
print '-' * 15
'''
import sys

def readfile(filename):
	''''''Print a file to the standard output''''''
	
	f = file(filename)
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,

	f.close()

#Script starts from here
if len(sys.argv) < 2:
	print 'No action specified'
	sys.exit()

if sys.argv[1].startswith('--'):
	option = sys.argv[1][2:]
	
	if option == 'version':
		print 'Version 1.2'
	elif option == 'help':
		print '''
#This program prints files to the standard output.
#Any number of files can be specified.		
#Option include:
#--version : Prints the version number
#--help:	Display this help
'''
	else:
		print 'Unknown option'
else:
	for filename in sys.argv[1:]:
		readfile(filename)
'''
print '''
sys:
	sys 模块包含系统对应的功能
	sys.argv 参数列表
	sys.exit 推出正在运行的程序
	sys.version 提供安装的Python的版本信息
	sys.version_info 元组 提供一个更简单的方法
	sys.stdin sys.stdout sys.stderr 对应程序的标准输入 标准输出 标准错误
os:
	os模块包含普遍的操作系统功能，对于平台无关的程序相当重要
	os.sep	操作系统特定的路径分隔符
	os.name 正在使用的平台
	...
'''
	
	
