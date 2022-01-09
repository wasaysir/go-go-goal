from flask_wtf import FlaskForm, RecaptchaField
from wtforms import Form, BooleanField, StringField, TextAreaField, SubmitField, EmailField, PasswordField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class signUp(FlaskForm):
    email = StringField(
        'Email',
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )
    username = StringField(
        'Username',
        [DataRequired()]
    )
    password1 = PasswordField(
        'Password',
        [DataRequired(),
        Length(min=7,
            message=('Your message is too short.')),
        EqualTo('password2', message='Passwords must match')]
    )
    password2 = StringField(
        'Password Confirmation',
        [DataRequired(),
        Length(min=4,
            message=('Your message is too short.'))]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search = StringField(
        'Username',
        [DataRequired()]
    )
