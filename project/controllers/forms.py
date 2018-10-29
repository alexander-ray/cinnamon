from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, InputRequired


# https://github.com/realpython/flask-registration/
# http://flask.pocoo.org/docs/1.0/patterns/wtforms/
class SignupForm(Form):
    username = StringField(
        'username',
        validators=[DataRequired(), Length(min=6, max=255)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=255)]
    )


# https://github.com/realpython/flask-registration/
# http://flask.pocoo.org/docs/1.0/patterns/wtforms/
class LoginForm(Form):
    username = StringField(
        'username',
        validators=[InputRequired(), Length(min=6, max=255)]
    )
    password = PasswordField(
        'password',
        validators=[InputRequired(), Length(min=6, max=255)]
    )
