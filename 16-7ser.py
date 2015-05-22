#!/usr/bin/env python
# File Name: 16-7ser.py

from time import ctime
from socket import *

HOST = ''
PORT = 21456
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
ans = getservbyname('daytime','tcp')
addr1 = addr2 = () 
while True:
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    print '[%s] %s'%(data, addr)

    if addr1 == addr and addr2:
        udpSerSock.sendto('[%s] %s'%(ctime(), data), addr2)
    elif addr2 == addr and addr1:
        udpSerSock.sendto('[%s] %s'%(ctime(), data), addr1)
    elif not addr1:
        addr1 = addr
        udpSerSock.sendto('', addr)
    elif not addr2:
        addr2 = addr
    else:
        continue

udpSerSock.close
