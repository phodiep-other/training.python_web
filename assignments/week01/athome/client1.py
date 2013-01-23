import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
server_address = ('localhost', 50000)
client.connect(server_address)

try:
    int1, int2 = 6, 7
    tmpString = str(int1)+','+str(int2)
    client.sendall(tmpString)
    print('Received from Server: ' + str(client.recv(100)))

finally:
    client.close()

