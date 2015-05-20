#!/usr/bin/env python
# File Name: tsTclntTW.py

from twisted.internet import protocol, reactor

HOST = 'locathost'
PORT = 21586 

class TSClntProtocol(protocol.Protocol):
	def sendData(self):
		data = raw_input(':')
		if data:
			print '...sending %s...'%data
			self.transport.write(data)
		else:
			self.transport.loseConnection()
			print 'connection colsed'
	def dataReceived(self,data):
		print 'dataReceived'
		print data
		self.sendData()
	def connectionMade(self):
		print 'start to connect'
		self.sendData()

class TSClntFactory(protocol.ClientFactory):
	protocol = TSClntProtocol
	clientConnectLost = clientConnectionFailed = \
			lambda self, connector, reason:reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
