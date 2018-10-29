from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import Length, InputRequired, NumberRange


class BaseUserForm(Form):
    username = StringField(
        'Username',
        validators=[InputRequired(), Length(min=6, max=255)]
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=255)]
    )


class BaseAddressForm(Form):
    street_address = StringField(
        'Street Address',
        validators=[InputRequired()]
    )
    city = StringField(
        'City',
        validators=[InputRequired()]
    )
    state = StringField(
        'State',
        validators=[InputRequired()]
    )
    zip = StringField(
        'Zip Code',
        validators=[InputRequired()]
    )


# https://github.com/realpython/flask-registration/
# http://flask.pocoo.org/docs/1.0/patterns/wtforms/
class SignupForm(BaseUserForm, BaseAddressForm):
    income = IntegerField(
        'Income',
        validators=[NumberRange(min=0, max=100000000)]
    )


