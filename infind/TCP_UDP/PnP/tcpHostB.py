import socket                   # Import socket module

B_host = '127.0.0.1'                 # Get local machine name
B_port = 50000                       # Reserve a port for your service.

A_port = 50001                        # Reserve a port for your service.
A_host = '127.0.0.1'

socket = socket.socket()             # Create a socket object

with open('received_tcp.jpg', 'wb') as f:
    print ('file opened')
    
    socket.bind((B_host, B_port))            # Bind to the port
    socket.listen(5)                         # Now wait for client connection.

    while True:
        conn, addr = socket.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        data = conn.recv(1024)
        #print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
socket.close()
print('connection closed')


filename='received_tcp.jpg'
f = open(filename,'rb')

socket.connect((A_host, A_port))

l = f.read(1024)
while (l):
    socket.send(l)
    l = f.read(1024)
f.close()
socket.close()

