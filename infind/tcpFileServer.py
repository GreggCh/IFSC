# server3.py on EC2 instance
import socket
from threading import Thread
from SocketServer import ThreadingMixIn

# TCP_IP = 'localhost'
TCP_IP = socket.gethostbyaddr("54.209.33.15")[0]
TCP_PORT = 5000
BUFFER_SIZE = 1024
FILE_NAME = "aula_TCP.txt"

print ('TCP_IP=',TCP_IP)
print ('TCP_PORT=',TCP_PORT)

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print ("New thread started for "+ip+":"+str(port))

    def run(self):
        f = open(FILE_NAME, 'w+')
        data = self.sock.recv(BUFFER_SIZE)
        f.write(data)

        print ("Openning file: " + FILE_NAME)
        f = open(FILE_NAME,'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                self.sock.send(" - DONE!")
                f.close()
                self.sock.close()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #STREAM -  tipo de mensagem do protocolo TCP
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print ("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print ('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
