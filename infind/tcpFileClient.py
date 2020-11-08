# client3.py on local machine
#!/usr/bin/env python

#!/usr/bin/env python

import socket
import time

#TCP_IP = 'localhost'
TCP_IP = '54.209.33.15'
TCP_PORT = 5000

BUFFER_SIZE = 1024
buf = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

f = open("Send_TCP.txt", "rb")
data = f.read(buf)
print("Sending...")
s.send(data)

with open('Received_TCP.txt', 'wb') as f:
    print('file opened')
    while True:
        #print('receiving data...')
        data = s.recv(1024)
        #print('data=%s', (data))
        if not data:
            f.close()
            print('file close()')
            break
        # write data to a file
        f.write(data)

print('Successfully get the file')
s.close()
print('connection closed')