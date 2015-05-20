#!/usr/bin/env python
# File Name: /home/angli/workspace/testsocket/socketser.py

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 12456 
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
	def handle(self):
		print '...connected from:', self.client_address
		self.wfile.write('[%s] %s'%(ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
