import socket
import sys

server = socket.socket(2,1,0)
server_address = ('localhost', 50000)
server.bind(server_address)

server.listen(1)

while True:
    con, cli = server.accept()

    try:
        int1, int2 = con.recv(100)
        intsum = int(int1) + int(int2)
        print('Received from Client: ' + int1 +' and '+ int2)
        con.sendall(str(intsum))

    finally:
        con.close()
        break

