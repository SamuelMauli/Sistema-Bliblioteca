from sqlalchemy import Column, Integer, String, Float
from ..database import db

class Book(db.Model):
    __tablename__ = 'livros'  # nome da tabela no banco de dados

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)  # ajuste o tamanho conforme necessário
    autor = Column(String(100), nullable=False)
    ano_publicacao = Column(Integer)
    preco = Column(Float)

