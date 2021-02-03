# ----- sender.py ------

#!/usr/bin/env python

from socket import *
import sys
import hashlib

def get_digest(file_path):
    h = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = 124
buf = 1024
addr = (host,port)

#file_name=sys.argv[2]
file_name = b"pingpong.jpg"
print(get_digest(file_name))

s.sendto(file_name,addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        data = f.read(buf)


s.close()
f.close()

socket_receiver = socket(AF_INET,SOCK_DGRAM)
socket_receiver.bind(("127.0.0.1",1080))

addr = ("127.0.0.1",1080)
buf=1024
data, addr = s.recvfrom(buf)
print(data)

socket_receiver.close()