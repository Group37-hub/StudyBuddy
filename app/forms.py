from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, IntegerField, DateField
from wtforms.fields.simple import StringField, PasswordField, HiddenField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
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

