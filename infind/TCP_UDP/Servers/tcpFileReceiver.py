# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import hashlib
import os

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
port = 8000

s = socket(AF_INET, SOCK_STREAM) #estou dizendo que vou usar o TCP na camada de transporte
s.bind((host,port))

addr = (host,port)
buf=1024

while(True):
    print ("Pronto para receber dados...")
    s.listen(5)
    c, addr = s.accept()
    data = c.recv(buf)
    print ("Received File:", data)
    file_name = data.decode('utf-8')
    c.send(b"Send the data!")
    f = open(file_name,'wb')

    data = c.recv(buf)
    while(data):
        print("Receiving...") 
        f.write(data)
        data = c.recv(buf)    
    f.close()
    c.close()
    print ("File Downloaded")

    hash_file = file_name[0:-4] + "_hash.txt"
    f = open(hash_file.encode('utf-8'),'wb')
    f.write(get_digest(file_name).encode('utf-8'))
    f.close()