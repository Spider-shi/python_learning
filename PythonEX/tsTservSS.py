#! /usr/lib/python

from SocketServer import (TCPServer, StreamRequestHandler)
from time import ctime

HOST = ''
PORT = 19887
ADDR = (HOST, PORT)

class myStreamRequestHandler(StreamRequestHandler):
	def handle(self):
		print '...connected from:', self.client_address
		self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = TCPServer(ADDR, myStreamRequestHandler)
print 'waiting for connecting...'
tcpServ.serve_forever()
