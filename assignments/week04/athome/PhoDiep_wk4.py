#!/usr/bin/python

def get_titles():
    
    html = """<html>
<head>
<title>Pho Diep - Week4 Homework</title>
</head>
<h1>List of Python Books</h1>
<body> %s
</body>
</html>"""

    temp = ''
    for entry in bookList.titles():
        temp_href= '<a href="/?id='+ str(entry['id']+'">')
        temp += str(temp_href + entry['title'] + '</a><br>' + '<br>')

    return html % temp

def get_bookinfo(id):

    try:
        book = bookList.title_info(str(id))
    
        html = """<html>
<head>
<title>Pho Diep - Week4 Homework</title>
</head>
<h2>%s</h2>
<body>
ISBN: %s <br>
Publisher: %s <br>
Author: %s <br>
<br>
<a href="../"> Return to Book List</a>
</body>
</html>"""


        return html % (book['title'],
                       book['isbn'],
                       book['publisher'],
                       book['author'])
    
    except:
        return """<html>
    <body> Sorry, this book could not be found. <br>
    <a href="../"> Return to Book List</a>
    </body>
    </html>"""

def application(environ, start_response):
    from cgi import parse_qs
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    book_id = parameters.get('id')
    if book_id == None:
        response_body = get_titles()
    else:
        response_body = get_bookinfo(book_id[0])
    
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    from bookdb import BookDB
    bookList = BookDB()
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
else:
    import sys
    sys.path.append('usr/lib/wsgi-bin')
    from bookdb import BookDB
    bookList = BookDB()
