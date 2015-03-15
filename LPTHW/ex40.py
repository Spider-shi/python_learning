#! /usr/lib/python
# Filename  : ex40.py

class Song:
	
	accout = 0

	def __init__(self, lyrics):
		self.lyrics = lyrics
		Song.accout += 1

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def __del__(self):
		self.__class__.accout -= 1
		
happy_birthday_song = Song(['Happy birthday to u. \
I don\'t want get sued. \
So I\'ll stop right there.', 'hello world'])

happy_birthday_song.sing_me_a_song()

Song.accout += 10

print Song.accout

print happy_birthday_song.lyrics
