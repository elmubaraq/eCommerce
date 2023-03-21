from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Length,EqualTo, Email, DataRequired, ValidationError
from market.models import User
class RegistrationForm(FlaskForm):
     def validate_username(self,username_to_check):
          user = User.query.filter_by(username=username_to_check.data).first()
          if user:
               raise ValidationError('Username already taken')
     def validate_email_address(self,email_to_check):
          email= User.query.filter_by(email_address=email_to_check.data).first()
          if email:
               raise ValidationError('Email already exist, try forget password')
     username  = StringField(label='Username: ', validators=[Length(min=2,max=30),DataRequired()])
     email_address = StringField(label='Email:', validators=[Email(),DataRequired()])
     password1 = PasswordField(label='Password', validators=[Length(min=8),DataRequired()])
     password2 = PasswordField(label='Verify password', validators=[EqualTo('password1'),DataRequired()])
     submit = SubmitField(label='Create account')
     
class LoginForm(FlaskForm):
     username = StringField(label='Username:', validators=[DataRequired()])
     password = StringField(label='password:', validators=[DataRequired()])
     submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
     submit = SubmitField(label='Purchase!')
     
class SellItemForm(FlaskForm):
     submit = SubmitField(label='Sell Item!')
     
     
     
     