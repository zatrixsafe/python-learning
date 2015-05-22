#!/usr/bin/env python
# File Name: 16-7cli.py
from socket import *

HOST = 'localhost'
PORT = 21456
ADDR = (HOST, PORT)
BUFSIZ = 1024

udpCliSock = socket(AF_INET, SOCK_DGRAM)
data = ''
udpCliSock.sendto(data,ADDR)
while True:
    data,addr = udpCliSock.recvfrom(BUFSIZ)
    if data:
        print '[%s], %s'%(addr, data)
    data = raw_input('>')
    udpCliSock.sendto(data,ADDR)
udpCliSock.close()
