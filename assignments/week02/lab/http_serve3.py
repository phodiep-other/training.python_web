#!/usr/bin/env python

import socket
import time
import email.utils

def ok_response(body):
    firstline = "HTTP/1.1 200 OK"
    header = "Content-Type: text/html "
    empty = ""
    resp = "\r\n".join([firstline, header, empty, body])
    return resp

def parse_request(request):
    """return link after GET"""
    print request
    uri = request[0]
    #print uri
    return uri

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    dataFile = open("tiny_html.html")
    data = dataFile.read()
    dataFile.close()

    #data = client.recv(size)
    if data: # if the connection was closed there would be no data
        print "received: %s, sending it back"%data
        print email.utils.formatdate()
        print parse_request(data)
        #time.sleep( 0.5)
        client.send(ok_response(data)) 
        client.close()
