from flask import Flask
from dotenv import load_dotenv
import os
from markupsafe import escape

# Set up the environment variables from a .env file in the current directory - add FLASK_APP=main.py to .env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)

@app.route("/")
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

@app.route('/path/<path:subpath>')
def show_subpath(subpath: str):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

if __name__ == "__main__":
    app.run(debug=True)