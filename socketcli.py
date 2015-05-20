#!/usr/bin/env python
# File Name: /home/angli/workspace/testsocket/socketcli.py

from socket import *

HOST = 'localhost'
PORT = raw_input('the port:')
if not PORT:
    PORT = 12456 
else:
    PORT = int(PORT)
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	data = raw_input(':')
	if not data:
		break
	tcpCliSock.send('%s\r\n'%data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data.strip()
tcpCliSock.close()
