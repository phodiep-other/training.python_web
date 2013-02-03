#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import datetime


print "Content-Type: text/html"
print

body = """<html>
<head>
<title>Lab 1 - CGI experiments</title>
</head>
<body>
The server name is %s. (if an IP address, then a DNS problem) <br>
<br>
The server address is %s:%s.<br>
<br>
Your hostname is %s.  <br>
<br>
You are coming from  %s:%s.<br>
<br>
The currenly executing script is %s<br>
<br>
The request arrived at %s<br>

</body>
</html>""" % (
        os.environ['SERVER_NAME'], # Server Hostname
        os.environ.get('SERVER_ADDR','aaaa'), # server IP
        os.environ.get('SERVER_PORT','bbbb'), # server port
        os.environ.get('REMOTE_HOST','cccc'), # client hostname
        os.environ.get('REMOTE_ADDR','dddd'), # client IP
        os.environ.get('REMOTE_PORT','eeee'), # client port
        os.environ.get('SCRIPT_NAME','ffff'), # this script name
        str(datetime.datetime.now()), # time
        )

print body,
