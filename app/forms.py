from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, IntegerField, DateField
from wtforms.fields.simple import StringField, PasswordField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class BookingForm(FlaskForm):
    room_id = SelectField(validators=[DataRequired()], coerce=int)
    user1_id = IntegerField(validators=[DataRequired()])
    user2_id = IntegerField(validators=[DataRequired()])
    week_beginning = DateField(validators=[DataRequired()])
    day = SelectField('Day', choices=[
        (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'),
        (4, 'Friday')
    ], coerce=int, validators=[DataRequired()])
    hour = SelectField('Hour', choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Book Room')

class InvitationResponseForm(FlaskForm):
    accept = SubmitField('Accept')
    decline = SubmitField('Decline')

class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        if not email.data.endswith('@student.bham.ac.uk'):
            raise ValidationError('Email must end with @student.bham.ac.uk')

