from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, length
from flask_wtf import FlaskForm

class SignupForm(FlaskForm):
    username = StringField("UserName", validators=[DataRequired(),])
    phonenumber = StringField("Phone Number", validators=[DataRequired()])
    driftcar = StringField("DriftCar", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("UserName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired(), length(max=300) ])
    submit = SubmitField("Submit")

class CheckForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])