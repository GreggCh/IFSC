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


s = socket(AF_INET,SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])
buf = 1024
addr = (host,port)

file_name=sys.argv[3]
#file_name = b"imagem.jpg"
print(get_digest(file_name))
f=open(file_name,"rb")

print("Sending: "+ file_name)
s.connect(addr)
s.send(file_name.encode('utf-8'))
print("Waiting for confirmation to send data...")
resposta = s.recv(1024)
print(resposta.decode('utf-8'))
print("Sending data...")
data = f.read(buf)
while (data):
    print("Sending...")
    s.send(data)
    data = f.read(buf)
print("Upload ended")
s.close()
f.close()