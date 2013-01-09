import socket
import sys

server = socket.socket(2,1,0) # Create a TCP/IP socket

server_address = ('localhost', 50000)
server.bind(server_address) # Bind the socket to the port

server.listen(1) # Listen for incoming connections

while True:
    con, cli = server.accept() # Wait for a connection

    try:
        message = con.recv(42) # Receive the data and send it back
        print (message)
        con.sendall(message)

    finally:
        con.close() # Clean up the connection
        break



