from flask import Blueprint, render_template
from ..database import db
from ..models.book import Book

books = Blueprint('books', __name__)

@books.route('/books')
def list_books():
    books = Book.query.all()
    return render_template('books.html', books=books)
