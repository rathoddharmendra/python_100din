from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/health')
def health_check():
    return 'OK'

if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0')