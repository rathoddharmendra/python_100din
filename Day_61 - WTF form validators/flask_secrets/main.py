from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
SECRET_KEY = 'my super secret key'.encode('utf8')
app.secret_key = SECRET_KEY

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
    # name = StringField('name', validators=[DataRequired()])
    # email = StringField('email', validators=[DataRequired()])



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    my_form = MyForm()
    my_form.validate_on_submit()
    return render_template('login.html', form=my_form)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    my_form = MyForm()
    if my_form.validate_on_submit():
        print(my_form)
        return render_template('success.html')
    
    print(my_form.name.data)
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
