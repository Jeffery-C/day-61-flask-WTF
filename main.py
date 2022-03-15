from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
import os

# pip install email-validator


class MyForm(FlaskForm):
    email = StringField(label="email",
                        validators=[DataRequired(),
                                    validators.Email(),
                                    validators.Length(min=6, message="Little short for an email address?")])
    password = PasswordField(label="password",
                             validators=[DataRequired(),
                                         validators.Length(min=8, message="Field must be at least 8 characters long.")])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')


# @app.route("/login")
# def login():
#     return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    form.validate_on_submit()

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
