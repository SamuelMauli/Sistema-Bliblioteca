from flask import Blueprint, render_template, request, redirect, url_for
from ..database import db
from ..models.user import User

auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return redirect(url_for('books.list_books'))  # Redireciona após o login
    return render_template('login.html')

