#! /user/bin/python
# Filename : ex31.py

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake . What do you do?"
	print "1.Take the cake."
	print "2.Scream at the bear."

	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eat your face off. Good Job!"
	elif bear == "2":
		print "The bear eat your legs off. Good Job!"
	else:
		print "Well. doing %s is pribably better. Bear runs away." % bear

elif door =="2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1.Blueberries."
	print "2.Yellow jacket clothespins."
	print "3.Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survies powered by a mind of jello. Good Job."
	else:
		print "The insanity rots your eyes into a pool of muck. Good Job."

else:
	print "You stumble around and fall on a knife and die. Good Job!"
