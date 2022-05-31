# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import hashlib
from datetime import datetime

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

host = "172.16.0.51"  
port = 8000

print ('UDP server running on ' + host + 'and port > ' + str(port))

while(True):

    log = "UDP >>"

    s = socket(AF_INET,SOCK_DGRAM) #estou dizendo que vou usar o UDP na camada de transporte
    s.bind((host,port))

    addr = (host,port)
    buf=1024
    data, addr = s.recvfrom(buf)
    print ("Received File:", data)

    file_name = data.decode('utf-8')
    s.sendto(b"Send the data!", addr)
    f = open(file_name,'wb')
    data,addr = s.recvfrom(buf)
      
    try:
        while(data != b"\r"):
            f.write(data)
            s.settimeout(0.2)
            data,addr = s.recvfrom(buf)
        f.close()
        s.sendto(b"End of receiving data.", addr)
        print ("File Downloaded")
    except timeout:
        s.sendto(b"Timeout of 200ms exceeded!", addr)
        f.close()

    hash_file = file_name[0:-4] + "_hash.txt"
    f = open(hash_file.encode('utf-8'),'wb')
    f.write(get_digest(file_name).encode('utf-8'))
    f.close()
    s.close()

    now = datetime.now()      # Save the time
    current_time = now.strftime("%H:%M:%S")

    log = log + "\tFile name:\t" + file_name + "\tat\t" + str(current_time) + "\n"

    with open('../log.txt', 'a') as f:
      f.write(log)