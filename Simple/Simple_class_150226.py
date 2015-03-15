#-*-coding:utf-8-*-
print '01'
print '-' * 15

'''
class Person:
	
	population = 0 #类的变量
	
	def __init__(self, name):#对象的变量
		self.name = name
		
		Person.population += 1
	def __del__(self):
		print '%s had go out' % self.name

		self.__class__.population -= 1#之所以这样写是因为python的内存回收机制 具体的不理解 先这样#
	
		if self.__class__.population == 0:
			print 'no people'
		else:
			print '%d people' % self.__class__.population

	def howMany(self):
		if Person.population == 0:
			print 'no people'
		else:
			print '%d people' % Person.population

bob = Person('bob')

bob.howMany()

jeely = Person('jeely')

jeely.howMany()
'''

print '02'
print '-' * 15

#类的继承
class SchoolMember:

	'''Represents any school member '''

	def __init__(self, name, age):
		self.name = name
		self.age = age
		
		print '(Initialized SchoolMember: %s)' % self.name
	
	def tell(self):
		'''Tell my details'''
		print 'Name : %s, Age : %s' % (self.name, self.age)

class Teacher(SchoolMember):
	'''Represents a teacher'''
	
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary

		print 'Initialized Teacher: %s' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: %d' % self.salary

class Student(SchoolMember):
	'''Represent a student'''
	
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		
		print 'Initialized Student: %s' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: %s' % self.marks					


t = Teacher('Mr.Shaw', 23, 8000)
s = Student('Jelly', 12, 'G')

#t.tell()
#s.tell()

members = [t, s]
for member in members:
	member.tell()

print SchoolMember.__doc__
print Teacher.__doc__
print Student.__doc__

print SchoolMember.tell.__doc__
