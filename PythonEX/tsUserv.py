#! /usr/lib/python

from socket import *
import time

HOST = ''
PORT = 19888
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpServSock = socket(AF_INET, SOCK_DGRAM)
udpServSock.bind(ADDR)

while True:
	print 'waiting for message...'
	data, addr = udpServSock.recvfrom(BUFSIZE)
	udpServSock.sendto('[%s], %s' % (time.ctime(), data), addr)
	print '...received from and returned to ', addr

udpServSock.close()

