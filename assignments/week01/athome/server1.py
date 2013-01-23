import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
server_address = ('localhost', 50000)
server.bind(server_address)
server.listen(1)

while True:
    con, cli = server.accept()

    try:
        strRec = con.recv(100)
        int1, int2 = strRec.split(',')
        intsum = int(int1) + int(int2)
        print('Received from Client: ' + int1 +' and '+ int2)
        con.sendall(str(intsum))

    finally:
        con.close()
        break

server.close()
