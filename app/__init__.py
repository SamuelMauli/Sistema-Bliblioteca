from flask import Flask
from .database import db
from .routes.auth import auth as auth_blueprint
from .routes.books import books as books_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///identifier.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'sua_chave_secreta'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(books_blueprint)

    return app
