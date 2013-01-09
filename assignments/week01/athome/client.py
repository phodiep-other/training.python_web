import socket
import sys

client = socket.socket(2,1,0)
server_address = ('localhost', 50000)
client.connect(server_address)

try:
    int1, int2 = 6, 7
    client.sendall(str(int1))
    client.sendall(str(int2))
    print('Received from Server: ' + str(client.recv(100)))

finally:
    client.close()
