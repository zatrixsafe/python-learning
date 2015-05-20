#!/usr/bin/env python
# File Name: /home/angli/workspace/testsocket/udpclient.py

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 21567 
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = raw_input(">")
	if not data:
		break
	udpCliSock.sendto(data, ADDR)
	data, ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print data
udpCliSock.close()
