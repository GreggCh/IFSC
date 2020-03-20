# ----- sender.py ------

#!/usr/bin/env python

import socket
import sys
import select

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "34.210.45.213"
port = 7000
buf =1024
addr = (host,port)

file_name = "aula.txt"

print ("Sending file: " + file_name)

#s.sendto(file_name.encode(),addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print ("sending ..." + str(data))
        data = f.read(buf)
s.close()
f.close()