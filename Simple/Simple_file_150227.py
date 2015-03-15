#-*-coding:utf-8-*-
# 简明python教程 第12章 输入\输出
print '01'
print '-' * 15
'''
poem = '''
#Programming is fun
#When the work is done
#if you wanna make your work also fun:
#use python!
'''

f = file('poem.txt', 'w')

f.write(poem)

f.close
 
f = file('poem.txt')# if no mode is specified, 'r'ead mode is assumed by default

while True:
	line = f.readline()
	if len(line) == 0:
		break

	print line,

f.close()

'''

print '02'
print '-' * 15
'''
import cPickle 

shoplistfile = 'shoplist.data' #the name of the file where we will store the object

shoplist = ['apple', 'mango', 'carrot']

#write to the file
f = file(shoplistfile, 'w')
cPickle.dump(shoplist, f)  #dump a object to a file
f.close()

del shoplist

#Read back form the storage
f = file(shoplistfile)
storedlist = cPickle.load(f)

print storedlist

'''

print '''

文件的使用：
	打开文件 'r' 'w' 'a' 默认模式是'r'
	write() readline() close()

存储器：
	储存和去储存 Pickle cPickle
	cPickle.dump(object, file)
	cPickle.load(file)
'''

