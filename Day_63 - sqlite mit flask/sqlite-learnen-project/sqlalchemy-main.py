from flask import Flask, render_template #, request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, ForeignKey, Float
import os

db_path = os.path.join(os.path.dirname(__file__), 'new-books-collection.db')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # def __repr__(self) -> str:
    #     return f'<Book {self.title}>'

with app.app_context():
    db.create_all()

# with app.app_context():
#     book = Books(title='Clean New Code', author='Caro C. Jeffrey', rating=1.2)
#     db.session.add(book)
#     db.session.commit()

# Reads all Books from the database
with app.app_context():
    books = db.session.execute(db.select(Books).order_by(Books.title)).scalars().all()
    print([book.title for book in books])

# Read one row
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "New Code")).scalar()
    print(f'{book=}')

# Update a book in the database
# with app.app_context():
#     book_id = 1
#     book_to_update = db.get_or_404(Books, book_id)
#     book_to_update.title = 'New Code - updated'
# # OR find using where clause, 
#     book = db.session.execute(db.select(Books).where(Books.title == "New Code")).scalar()
#     book.title = 'New Code - updated'
#     db.session.commit()
# delete a book from the database
# with app.app_context():
#     book_id = 1
#     book_to_delete = db.get_or_404(Books, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()

