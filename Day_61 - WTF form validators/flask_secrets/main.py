from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, input_required, ValidationError
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import SelectField, SubmitField
from wtforms.widgets import SubmitInput
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
csrf = CSRFProtect(app)

WTF_CSRF_SECRET_KEY = 'a random string'

class MyForm(FlaskForm):
    class Meta:
        csrf = True
        locales = ('en_US', 'en')

    name = StringField(label='Name', validators=[DataRequired(), input_required()], name='name')
    email = StringField(label='Email', validators=[DataRequired()], name='email', description='We will never share your email with anyone else.')
    password = PasswordField(label='Password', validators=[DataRequired()], name='password')
    select = SelectField(label='Select', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], validators=[DataRequired()])
    accept_rules = BooleanField('I accept the site rules', [input_required()])
    submit = SubmitField(label='Submit')
    # go = SubmitInput('Go')



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    my_form = MyForm()
    return render_template('login.html', form=my_form)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    my_form = MyForm()
    if my_form.validate_on_submit():
        print('Form validated')
        print(my_form.data.items())
        return render_template('success.html')
    
    print('Form not validated')
    print(my_form.data.items())

    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
