# ----- receiver.py -----

#!/usr/bin/env python

import socket
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

host = "0.0.0.0"  
port = 8000


while(True):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
    except socket.timeout:
        f.close()
        s.close()
        print ("File Downloaded")

    f = open("hash.txt",'wb')
    f.write(get_digest("image.jpg").encode('utf-8'))
    f.close()
    s.close()


    ss = socket.socket()             # Create a socket object
    ss.bind((host, port))            # Bind to the port
    ss.listen(5)                     # Now wait for client connection.

    print ('Server listening...')

    conn, addr = ss.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received request to open:', data.decode('utf-8'))
    
    filename = data.decode('utf-8')
    if os.path.exists(filename):
      f = open(filename,'rb')
      l = f.read(1024)
      while (l):
        conn.send(l)
        l = f.read(1024)
      f.close()
    else:
      conn.send(b"There is no hash file. Upload the image.jpg via UDP first to generate the hash file.")
    conn.close()

    if (filename != "pingpong.jpg"):   
      if (os.path.exists(filename)):
        os.remove(filename)
      else:
        print("The file does not exist")
    
    ss.close()
