# ----- sender.py ------

#!/usr/bin/env python

from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host = "34.210.45.213"
port = 7000
buf =1024
addr = (host,port)

file_name = "mytext2.txt"

s.sendto(file_name.encode(),addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print ("sending ...")
        data = f.read(buf)
s.close()
f.close()
has_dualstack_ipv6()