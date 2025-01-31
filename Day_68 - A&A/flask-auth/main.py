from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

db_path = os.path.join(os.path.dirname(__file__), 'instance/users.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['UPLOAD_FOLDER'] = 'static/files'

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


app = Flask(__name__)

# @app.route('/register', methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         # Hashing and salting the password entered by the user 
#         hash_and_salted_password = generate_password_hash(
#             request.form.get('password'),
#             method='pbkdf2:sha256',
#             salt_length=8
#         )
#         # Storing the hashed password in our database
#         new_user = User(
#             email=request.form.get('email'),
#             name=request.form.get('name'),
#             password=hash_and_salted_password,
#         )

#         db.session.add(new_user)
#         db.session.commit()

#         return render_template("secrets.html", name=request.form.get('name'))

#     return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.debug = True
    app.run()


# generate_password_hash(password, method='sha256')
# Check if user already exists
# user = User.query.filter_by(email=email).first()
# if user:
#     flash('User already exists')
    # https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.security.check_password_hash
