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
host = sys.argv[1]
port = 124
buf = 1024
addr = (host,port)

file_name=sys.argv[2]
#file_name = b"imagem.jpg"
print(get_digest(file_name))

f=open(file_name,"rb")

s.sendto(file_name.encode(),addr)

data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        data = f.read(buf)

s.sendto(b"\r",addr)
resposta = s.recvfrom(1024)
print(resposta)
s.close()
f.close()