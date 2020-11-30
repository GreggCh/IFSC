import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 31337
f = open("send_UDP.txt", "r")

MESSAGE = bytes(f.read(), 'utf-8')

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '127.0.0.1'
server_port = 31338

server = (server_address, server_port)
sock.bind(server)

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print("received message: %s" % data)