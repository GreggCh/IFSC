# ----- receiver.py -----

#!/usr/bin/env python

import socket
import sys
import select

host = socket.gethostbyaddr("34.210.45.213")[0]
port = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(host, port)

addrHost = (host, port)
buf=1024

fileName, addrHost = s.recvfrom(buf)
print ("Received File:",fileName.strip())

f = open(fileName.strip(),'wb')

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
