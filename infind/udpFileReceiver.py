# ----- receiver.py -----

#!/usr/bin/env python

import socket
import sys
import select

host = socket.gethostbyaddr("34.210.45.213")[0]
port = 7000
FILE_NAME = "aula_UDP.txt"

while True:
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    addrHost = (host, port)
    buf=1024

    #fileName, addrHost = s.recvfrom(buf)
    #print ("Received File:",fileName.strip())

    data, addrHost = s.recvfrom(buf)

    sent = s.sendto("Echo", addrHost)

    f = open(FILE_NAME.strip(),"w+")
    try:
        while(data):
            print("receiving ..." + str(data))
            f.write(str(data))
            #s.settimeout(2)
            #data, addrHost = s.recvfrom(buf)
    except:
        data += " - DONE!"
        sent = s.sendto(data, addrHost)
        print ("File Downloaded")
        f.close()
        s.close()
