from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..database import db
from ..models.book import Book

books = Blueprint('books', __name__)

@books.route('/books')
def list_books():
    page = request.args.get('page', 1, type=int)  # Obter o número da página
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

@books.route('/books/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        book.titulo = request.form.get('titulo')
        book.autor = request.form.get('autor')
        book.ano_publicacao = request.form.get('ano_publicacao')
        book.preco = request.form.get('preco')

        db.session.commit()
        flash('Livro atualizado com sucesso!', 'success')
        return redirect(url_for('books.list_books'))

    return render_template('update_book.html', book=book)

@books.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Livro deletado com sucesso!', 'success')
    return redirect(url_for('books.list_books'))

@books.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')
    page = request.args.get('page', 1, type=int)  # Obter o número da página
    per_page = 5  # Número de livros por página

    books_query = Book.query.filter(Book.titulo.contains(query)).paginate(page=page, per_page=per_page)

    return render_template('books.html', books=books_query.items, page=books_query.page, total_pages=books_query.pages, query=query)
