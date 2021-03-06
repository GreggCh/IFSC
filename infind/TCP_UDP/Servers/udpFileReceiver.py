# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import hashlib
import os

pid = str(os.getpid())
currentFile = open('/tmp/udp.pid', 'w')
currentFile.write(pid)
currentFile.close()

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

host = "127.0.0.1"  
port = 9999


while(True):
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind((host,port))

    addr = (host,port)
    buf=1024
    data, addr = s.recvfrom(buf)
    print ("Received File:",data.strip())
    f = open("image.jpg",'wb')

    data,addr = s.recvfrom(buf)
    try:
        while(data):
            f.write(data)
            s.settimeout(2)
            data,addr = s.recvfrom(buf)
    except timeout:
        f.close()
        s.close()
        print ("File Downloaded")

    f = open("hash.txt",'wb')
    f.write(get_digest("image.jpg").encode('utf-8'))
    f.close()