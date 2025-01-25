from flask import Flask
from dotenv import load_dotenv
import os
from markupsafe import escape

# Set up the environment variables from a .env file in the current directory - add FLASK_APP=main.py to .env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def make_italics(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

def make_underline(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper
@app.route("/")
@make_underline
@make_bold
@make_italics
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "<p>Bye Bye!</p>"


@app.route('/user/<string:username>')
def show_user_profile(username: str):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>', methods=['POST']) # methods=['POST']
def show_subpath(subpath: str):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)