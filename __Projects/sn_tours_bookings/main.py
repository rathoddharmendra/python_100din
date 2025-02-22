from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print('form submitted')
        print(request.form.get('name'))
        # send an email here
    return render_template('contact.html')

# @app.route('/post/<int:blog_id>')
# def get_blog(blog_id: int):
#     data = requests.get(API_URL).json()[blog_id - 1]
#     # Your code here to iterate over the data and extract relevant information
#     return render_template("postit.html", post=data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    