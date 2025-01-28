from flask import Flask, render_template
import requests

app = Flask(__name__)
API_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
@app.route('/')
def home():
    response = requests.get(API_URL).json()
    # Your code here to iterate over the data and extract relevant information

    return render_template("index.html", blogs=response)


@app.route('/blog/<int:blog_id>')
def get_blog(blog_id: int):
    response = requests.get(API_URL).json()[blog_id - 1]
    # Your code here to iterate over the data and extract relevant information
    return render_template("post.html", blog=response)
if __name__ == "__main__":
    app.run(debug=True)
