#! /usr/lib/python

from socket import *

HOST = '172.24.16.175'
PORT = 25166
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = raw_input('>')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZE)
	if not data:
		break

	print data

tcpCliSock.close()
