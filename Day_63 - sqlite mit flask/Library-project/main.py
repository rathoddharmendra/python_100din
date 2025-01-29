from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, ForeignKey, Float

# from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
import os

db_path = os.path.join(os.path.dirname(__file__), 'books-collection.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# bootstrap = Bootstrap4(app)


class Book(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    title = StringField('Book Title', validators=[DataRequired()])
    author = StringField('Author Name', validators=[DataRequired()])
    rating = StringField('Ratings', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    author: Mapped[str] = mapped_column(String(30), nullable=False)
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


# view functions below
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

# simple version - allows rating to be updated
# @app.route("/edit/<int:book_id>/<string:title>/<string:author>/<float:rating>", methods=["GET", "POST"])
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id: int = -1):
    global all_books
    if book_id == -1 :
        book_id = int(request.form['id'])
    if request.method == 'POST':
        with app.app_context():
            book_to_update = db.get_or_404(Books, book_id)
            book_to_update.rating = request.form['rating']
            db.session.commit()

        all_books = update_books()
        return redirect(url_for('home'))
    with app.app_context():
        # book = db.get_or_404(Books, book_id).scalar()
        book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
        title = book.title
        author = book.author
        rating = book.rating
    return render_template("edit.html", book={'id': book_id, 'title': title, 'author': author, 'rating': rating})

# @app.route('/update', methods=["POST"])
# def update():
#     return edit()
# @app.route("/edit/<int:book_id>", methods=["GET", "POST"])
# def edit(book_id: int):
#     global all_books
#     form = Book()
#     if request.method == 'POST':
#         with app.app_context():
#             book_to_update = db.get_or_404(Books, book_id)
#             book_to_update.title = request.form['title']
#             book_to_update.author = request.form['author']
#             book_to_update.rating = request.form['rating']
#             db.session.commit()

#         all_books = update_books()
#         return redirect(url_for('home'))
#     return render_template("edit.html", form=form)
    

@app.route("/delete/<int:book_id>")
def delete(book_id: int):
    global all_books
    with app.app_context():
        book_to_delete = db.get_or_404(Books, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        all_books = update_books()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

