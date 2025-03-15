from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def submit():
    print(request.form['name'])
    return f'<h1> Form submitted successfully by {request.form['name']}</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5002)


    {
    "event_name": "Jagannatha Jagran",
    "event_detail": "Welcome to the night of Jagran!",
    "organised_by": "Sheral & Dee",
    "registration_details": "No registration required. All are welcome.",
    "event_date": "15.03.2025",
    "event_time": "20:00"
}