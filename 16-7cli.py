#!/usr/bin/env python
# File Name: 16-7cli.py
from socket import *

HOST = 'localhost'
PORT = 21456
ADDR = (HOST, PORT)
BUFSIZ = 1024

udpCliSock = socket(AF_INET, SOCK_DGRAM)
data = ''
while True:
    udpCliSock.sendto(data,ADDR)
    data,addr = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        print '[%s], %s'%(addr, data)
    data = raw_input('>')
udpCliSock.close()
