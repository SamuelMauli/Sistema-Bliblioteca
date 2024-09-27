from sqlalchemy import Column, Integer, String, Float
from ..database import db

class Book(db.Model):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(100), nullable=False)
    ano_publicacao = Column(Integer)
    preco = Column(Float)

    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco
