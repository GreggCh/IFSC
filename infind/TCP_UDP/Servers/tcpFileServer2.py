# server.py
import os
import socket                   # Import socket module

port = 60004                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = '127.0.0.1'    # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
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
