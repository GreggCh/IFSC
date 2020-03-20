# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select

host = "127.0.0.1"
port = 7001
s = socket(AF_INET,SOCK_DGRAM)
s.bind(host, port)

addrHost = (host, port)
buf=1024

data, addrHost = s.recvfrom(buf)
print ("Received File:",data.strip())
f = open("received_file.txt",'wb')

data, addrHost = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data, addrHost = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print ("File Downloaded")
