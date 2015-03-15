#-*-coding:utf-8-*-

print '01' 
print '-' * 15

#This is my shopping list
#shoplist = ['apple', 'mango', 'carrot', 'banana']

#print 'I have', len(shoplist), 'items to purchase.'

#print 'These items are:'

#for item in shoplist:
	#print item,

#print '\nI also have to buy rice.'

#shoplist.append('rice')

#print 'My shoplist now is:', shoplist

#print 'I will sort my list now.'
#shoplist.sort()

#print 'Sorted list is', shoplist

#print 'The first item I will buy is', shoplist[0]

#olditem = shoplist[0]

#del shoplist[0]

#print 'I have buy the', olditem

#print 'Now my shoplist is', shoplist

print '02'
print '-' * 15

#zoo = ('wolf', 'elephant', 'penguin')

#print "Number of animals in the zoo is", len(zoo)

#new_zoo = ('monkey', 'dolphin', zoo)

#print 'Number of animals in the new zoo is', len(new_zoo)

#print 'All animals in new zoo is', new_zoo

#print 'Animals brought from the old zoo is', new_zoo[2]

#print 'Last animal brought from old zoo is', new_zoo[2][2]

print '03'
print '-' * 15

#ab = {'Swaroop' : 'swaroopch@byteofpython.info', 
	#'Larry' : 'larry@wall.org', 
	#'Matsumoto' : 'matz@ruby-lang.org',
	#'Spammer' : 'spammer@hotmail.com'
#}

#print 'Swaroop\'s address is %s' % ab['Swaroop']

#Add a key/value pair
#ab['Guido'] = 'guido@python.org'

#delete a key/value pair
#del ab['Spammer']

#print 'There are %d contacts in the address-book.' % len(ab)

#for name, address in ab.items():
	#print 'Contact %s at %s' % (name, address)

#if 'Guido' in ab:
	#print 'Guido\'s address is %s' % ab['Guido']

print '04'
print '-' * 15

#shoplist = ['apple', 'carrot', 'mango', 'banana']
#print shoplist

#Indexing or 'Subscription' operation
#print 'Item 0 is', shoplist[0]
#print 'Item 1 is', shoplist[1]
#print 'Item 2 is', shoplist[2]
#print 'Item 3 is', shoplist[3]
#print 'Item -1 is', shoplist[-1]
#print 'Item -2 is', shoplist[-2]
#print 'Item -3 is', shoplist[-3]
#print 'Item -4 is', shoplist[-4]

#Slicing on a list
#print 'Item 1 to 3 is', shoplist[1:3]
#print 'Item 2 to end is', shoplist[2:]
#print 'Item 1 to -1 is', shoplist[1:-1]
#print 'Item strat to end is', shoplist[:]

#Slicing on a string
#name = 'swroop'

#print name
#print 'name is %d words.' % len(name)

#print 'characters 1 to 3 is', name[1:3]
#print 'characters 2 to end is', name[2:]
#print 'characters 1 to -1 is', name[1:-1]
#print 'characters start to end is', name[:]

#shoplist = ['apple', 'carrot', 'banana', 'mango']

#mylist = shoplist

#print shoplist
#print mylist

#del shoplist[0]

#print 'First del', shoplist
#print mylist

#mylist = shoplist[:]
#print shoplist 
#print mylist

#del mylist[0]

#print 'Second del', shoplist
#print mylist

#name = "Swaroop"

#if name.startswith('Swa'):
	#print "Yes, the string starts with 'Swa'"

#if 'a' in name:
	#print "Yes, it contains the string 'a'"

#if name.find('war'):
	#print "Yes, it contains the string 'war'"

#delimiter = '_*_'

#mylist = ['Brazil', 'Russia', 'India', 'China']

#print delimiter.join(mylist)

print '''
列表：
	有序 可以添加append  删除del 排序sort 查找
元组：
	和字符串一样不可以改变
	元组中只有一个对象的时候注意逗号的使用
词典：
	类似与c++中 map 键值对 key/value pair 添加 删除del 
	无序 
序列：
	列表 元组 字符串都是序列 可以使用Indexing or subscaiption
	有切片操作

参考：
	参考与对象 

字符串的一些操作：
	startswith in join
'''
