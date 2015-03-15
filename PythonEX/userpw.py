#! /usr/lib/python
#Filename : userpw.py

useroperator = '''
\'1\':userapply,
\'2\':userlogin,
\'q\':userexit
'''

userpw = {}

def userapply():
	while True:
		username = raw_input('Please input the account:')
		if username in userpw.keys():
			print 'The accout is exists'
			print 'Enter the \'q\' exit'
			continue
		elif username == 'q':
			return False
		else:
			userpassword = raw_input('Please input the password:')
			userpw[username] = userpassword
			print 'Successful'
			print 'The account is %s, the password is %s' % (username, userpw[username])
			break

	return True

def userlogin():
	while True:
		username = raw_input('Please input the accout:')
		if username not in userpw.keys():
			print 'The account is not exist.'
			print 'Enter the "q" exit'
			continue
		elif username == 'q':
			return False
		else:
			break

	while True:
		userpassword = raw_input('Please input the password:')
		if userpassword != userpw[username]:
			print 'Wrong Password'
			print 'Enter the "q" exit'
			continue
		elif userpassword == 'q':
			return False
		else:
			print 'Login Successfully'
			break

	return True
	
def main():
	while True:
		print useroperator
		operator = raw_input('->')

		if operator == '1':
			ret = userapply()
			if (not ret):
				exit()
			else:
				continue
		elif operator == '2':
			ret = userlogin()
			if (not ret):
				exit()
			else:
				continue		
		elif operator == 'q':
			exit()
		else:
			print 'Please enter again: '


if __name__ == '__main__':
	main()
