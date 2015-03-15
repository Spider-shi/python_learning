#! /usr/lib/python

from socket import *

HOST = '10.10.3.90'
PORT = 19888
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = raw_input('>')
	if not data:
		break
	udpCliSock.sendto(data, ADDR)
	data, ADDR = udpCliSock.recvfrom(BUFSIZE)
	if not data:
		break
	print data

udpCliSock.close()
