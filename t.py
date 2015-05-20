#!/usr/bin/env python
# File Name: t.py

from socket import *
from time import ctime

HOST = ''
PORT = 21508
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
print ADDR
while True:
    print 'waiting for connection'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connect from:',addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s'%(ctime(),data))
tcpCliSock.close()
tcpSerSock.close()
