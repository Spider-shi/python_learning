#-*-coding:utf-8-*-
#! /usr/lib/python

'''a = int(raw_input("enter a num:"))

if a > 0:
	print ' a > 0'
elif a < 0:
	print ' a < 0'
else:
	print ' a== 0' 

#s = raw_input("Enter a str: ")

#for item in s:
#	print item, 

#i = 0
#length = len(s)

#while i < length:
	#print s[i],
	#i += 1

list = [2, 4, 23, 43, 5]

length = len(list)

i = 0

sum = 0
while i < length:
	sum += list[i]
	i += 1

result = float(sum) / length	

print result

fsum = 0

for item in list:
	fsum += item

print float(fsum) / len(list)


while True:
	num = int(raw_input('Enter a num : '))
	
#	if num in range(100):
	if num > 0 and num < 100:
		print 'Successful'
		break
	else:
		print 'Wrong, again'


def getnum(n):
	sum = 0
	for i in range(n):
		temp = int(raw_input("Enter a num: "))
		sum += temp
	return sum 
	
while True:
	print''' '''
1、	 取五个数之和
2、	 取五个数的平均值
'X':	 退出
''' '''
	choose = raw_input(" Enter your choose: ")
	
	if choose == '1':
		print 'sum'
		print getnum(5)
	elif choose == '2':
		print 'average'
		print float(getnum(5)) / 5 
	elif choose == 'X':
		print 'Done'
		break
	else:
		print 'Wrong Enter'

'''

import string
alphas = string.letters + ('_')
nums = string.digits

print "Welcome to the Identifier Checker V1.0"
print "Testees must be at least 2 chars long"

myInput = raw_input("Enter the name : ")

'''
if len(myInput) > 1:
	if myInput[0] not in alphas:
		print "invalid: first sympol must be alphas"
	else:
		for otherChar in myInput[1:]:
			if otherChar not in alphas + nums:
				print "invalid: remaing symbols must be alphasmric"
				break
		else:
			print "Ok as an identifier"
'''

if len(myInput) < 1:
	print "Testees must be at least 2 chars long"
	exit()

if myInput[0] not in alphas:
	print "Invalid: first symbol must be in alphas"
	exit()

alphasmeric = alphas + nums

for otherChar in myInput[1:]:
	if otherChar not in alphasmeric:
		print "Invalid: remaining symbols must be alphasmeric"
		break
else:
	print "OK as an identifier"
