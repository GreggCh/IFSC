import socket                   # Import socket module
import sys
import time

print('Wellcome to the CHAT. Enjoy! Write "#exit" to close...')

s = socket.socket()             # Create a socket object
host = '127.0.0.1' 
#primeiro escuta e espera uma conexão  
port = 8889
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening...')
conn, addr = s.accept()
data = conn.recv(1024)
nick = data.decode()
print ('Got connection from', nick)
my_nick = sys.argv[1]
conn.send(my_nick.encode())
while True:    
    data = conn.recv(1024)
    print("#" + nick + ": " + data.decode())
    if data.decode() == "#exit":
        break
    data = input(">>:")
    conn.send(data.encode())
    if data == "#exit":
        break
    
s.close()
print('connection closed')