# server.py
import os
import socket                   # Import socket module
from datetime import datetime

port = 8883                   # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = '64.227.114.120'    
# host = "127.0.0.1" 

s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.


print ('TCP server runing on: ' + host + 'and listening on port > ' + str(port))
while True:
  
    log = "TCP >>"

    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)

    data = conn.recv(1024)    
    file_name = data.decode('utf-8')
    print('Server received request to open:', file_name)

    file_path = "../arquivos_trabalho/"+file_name
    
    if os.path.exists(file_path):
      f = open(file_path,'rb')
      l = f.read(1024)
      while (l):
        conn.send(l)
        l = f.read(1024)
      f.close()
    else:
      conn.send(b"There is no hash file. Upload the image.jpg via UDP first to generate the hash file.")
    conn.close()

    now = datetime.now()      # Save the time
    current_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    log = log + "\tFile name:\t" + file_name + "\tat\t" + str(current_time) + "\n"

    with open('../log.txt', 'a') as f:
      f.write(log)
    
    log = ""
     
    if (os.path.exists(file_path)):
      os.remove(file_path)
    else:
      print("The file does not exist")
