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
host = socket.gethostname()     # Get local machine name
port = 60003                    # Reserve a port for your service.

s.connect((host, port))

filename = sys.argv[1].encode('utf-8')
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
if os.path.exists("image.jpg"):
    print(get_digest("image.jpg"))