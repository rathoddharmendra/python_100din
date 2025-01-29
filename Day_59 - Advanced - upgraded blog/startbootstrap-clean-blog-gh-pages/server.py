from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = 'https://api.npoint.io/674f5423f73deab1e9a7'

@app.route('/')
def home():
    data = requests.get(API_URL).json()
    return render_template('index.html', blogs=data)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:blog_id>')
def get_blog(blog_id: int):
    data = requests.get(API_URL).json()[blog_id - 1]
    # Your code here to iterate over the data and extract relevant information
    return render_template("postit.html", post=data)

if __name__ == '__main__':
    app.run(debug=True)
    