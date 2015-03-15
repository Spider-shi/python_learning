
def func_tuple(t):
	print t
	t[0] = 'hello'
	print t

def func_list(l):
	print l
	l.pop()
	print l

def main():
	t = ('I', 'am', 'good')
	l = ['This', 'is', 'perfect']

	func_tuple(t)
#	func_list(l)

#	print l
	print t

if __name__ == '__main__':
	main()

