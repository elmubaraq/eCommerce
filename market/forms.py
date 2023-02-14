from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField

class RegistrationForm(FlaskForm):
     username  = StringField(label='Username: ')
     email_address = StringField(label='Email:')
     password1 = PasswordField(label='Password')
     password2 = PasswordField(label='Verify password ')
     submit = SubmitField(label='Create account')
     