import socket                   # Import socket module
import sys

print('Wellcome to the CHAT. Enjoy! Write "#exit" to close...')

s = socket.socket()             # Create a socket object
s2 = socket.socket()
host = '127.0.0.1'   
port = 8889

s.connect((host, port))
my_nick = sys.argv[1]
s.send(my_nick.encode())

data = s.recv(1024)
nick = data.decode()
print ('Confirmed connection from', nick)

while True:
    data = input(">>:")
    s.send(data.encode())
    if data == "#exit":
        break
    data = s.recv(1024)
    print("#" + nick + ": " + data.decode())
    if data.decode() == "#exit":
        break
    
s.close()
print('connection closed')