import socket                   # Import socket module
import hashlib
import sys
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


s = socket.socket()             # Create a socket object
host =sys.argv[1] 
port = 123                    # Reserve a port for your service.

s.connect((host, port))

filename = sys.argv[2].encode('utf-8')
s.send(filename)

with open(filename, 'wb') as f:
    print ('file opened')
    while True:
        data = s.recv(1024)
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
if (filename.decode('utf-8') != "hash.txt"):
    if os.path.exists(filename):
        print(get_digest(filename))