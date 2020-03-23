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

file_name = "Send_UDP.txt"

print ("Sending file: " + file_name)

#s.sendto(file_name.encode(),addr)

f=open(file_name,"rb")
data = f.read(buf)
while(data):
    if(s.sendto(data,addr)):
        print ("sending..." + str(data))
        data = f.read(buf)

print ("File sent")

f = open("Recieved_UDP","w+")
data = s.recvfrom(buf)
try:
    while (data):
        print("receiving ..." + str(data))
        f.write(str(data))
        s.settimeout(2)
        data, addrHost = s.recvfrom(buf)
except:
    s.close()
    f.close()