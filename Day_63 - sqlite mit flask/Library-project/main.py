from flask import Flask, render_template, request, redirect, url_for
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

def update_books():
    with app.app_context():
        all_books = db.session.execute(db.select(Books)).scalars().all()
        return all_books

all_books = update_books()

@app.route('/')
def home():
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global all_books
    if request.method == 'POST':
        # print(request.form.to_dict())
        # all_books.append(request.form.to_dict())
        new_book = Books(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
            all_books = update_books()
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

