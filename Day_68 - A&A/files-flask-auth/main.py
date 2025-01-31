from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)
# CREATE DATABASE
db_path = os.path.join(os.path.dirname(__file__), 'instance/users.db')

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static/files')
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
@login_required
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return render_template('secrets.html', name=current_user.name)
    if request.method == "POST":
        # Hashing and salting the password entered by the user 
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        # Storing the hashed password in our database
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )

        user = User.query.filter_by(email=request.form.get('email')).first()

        if user:
            flash(f"Email {request.form.get('email')} is already registered, please use another email address.")
            return redirect(url_for('register'))

        db.session.add(new_user)
        db.session.commit()
        user = User.query.filter_by(email=request.form.get('email')).first()
        login_user(user)
        return render_template('index.html')

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return render_template('secrets.html', name=current_user.name)
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Email does not exist, please try again.")
            return redirect(url_for('login'))

        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for('login'))

        else:
            login_user(user)
            return render_template('secrets.html', name=user.name)
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("index.html")


@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf', as_attachment=True)



if __name__ == "__main__":
    app.run(debug=True)
