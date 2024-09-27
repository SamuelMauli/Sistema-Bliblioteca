from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..database import db
from ..models.book import Book

books = Blueprint('books', __name__)

@books.route('/books')
def list_books():
    page = request.args.get('page', 1, type=int)  # Número da página da página
    per_page = 5  # Número de livros por página
    books_query = Book.query.paginate(page=page, per_page=per_page)

    return render_template('books.html', books=books_query.items, page=books_query.page, total_pages=books_query.pages)

@books.route('/books/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        ano_publicacao = request.form.get('ano_publicacao')
        preco = request.form.get('preco')

        new_book = Book(titulo=titulo, autor=autor, ano_publicacao=ano_publicacao, preco=preco)
        db.session.add(new_book)
        db.session.commit()
        flash('Livro adicionado com sucesso!', 'success')
        return redirect(url_for('books.list_books'))

    return render_template('add_book.html')

