import socket
import sys

client = socket.socket(2,1,0) # Create a TCP/IP socket

server_address = ('localhost', 50000)
client.connect(server_address) # Connect the socket to the port where the server is listening

try:
    message = 'This is the message.  It will be repeated.'
    client.sendall(message)# Send data

    print client.recv(42) # print the response

finally:
    client.close() # close the socket to clean up
