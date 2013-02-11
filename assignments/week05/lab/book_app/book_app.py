from flask import Flask, render_template, url_for
import bookdb

app = Flask(__name__)

db = bookdb.BookDB()

@app.route('/')
def books():
    # put code here that provides a list of books to a template named 
    # "book_list.html"
    listBooks = db.titles()
    
    for entry in listBooks:
        entry['url'] = url_for('book', id=entry['id'])
    
    return render_template('book_list.html',name = listBooks)


@app.route('/book/<book_id>/')
def book(book_id):
    # put code here that provides the details of a single book to a template 
    # named "book_detail.html"
    singleBook = db.title_info(book_id)
    
    return render_template('book_detail.html', name = singleBook)


if __name__ == '__main__':
    app.run(debug=True)
