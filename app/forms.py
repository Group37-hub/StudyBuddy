from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.fields.simple import StringField, PasswordField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')