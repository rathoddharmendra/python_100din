from flask import Flask, render_template, request
from conn import Connection
from db import generate_cursor


app = Flask(__name__)

email = Connection()
db_cursor, db_conn = generate_cursor()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # send an email here

    return render_template('contact.html')

# @app.route('/post/<int:blog_id>')
# def get_blog(blog_id: int):
#     data = requests.get(API_URL).json()[blog_id - 1]
#     # Your code here to iterate over the data and extract relevant information
#     return render_template("postit.html", post=data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    