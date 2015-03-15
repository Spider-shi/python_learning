#! /user/bin/python
# Filename : ex39.py

class Song:
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bady = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bady.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

heart = Song("My heart")

class Person:
	def __init__(self, name):
		self.name = name

	def sayHi(self):
		print "Hi, my name is %s." % self.name

Bob = Person("Bob")

Bob.sayHi()
