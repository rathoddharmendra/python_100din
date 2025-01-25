from flask import Flask
from dotenv import load_dotenv
import os

print(os.__name__)
# Set up the environment variables from a .env file in the current directory - add FLASK_APP=main.py to .env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "<p>Bye Bye!</p>"

if __name__ == "__main__":
    app.run(debug=True)