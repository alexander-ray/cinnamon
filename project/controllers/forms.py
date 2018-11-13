from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SelectField, DateField, DecimalField
from wtforms.validators import Length, InputRequired, NumberRange
from datetime import datetime


class BaseUserForm(Form):
    username = StringField(
        'Username',
        validators=[InputRequired(), Length(max=255)]
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
        validators=[InputRequired(), NumberRange(min=0, max=100000000)]
    )


class SettingsForm(BaseAddressForm):
    income = IntegerField(
        'Income',
        validators=[InputRequired(), NumberRange(min=0, max=100000000)]
    )
    report_type = SelectField(
        'Report Type',
        coerce=str,
        validators=[InputRequired()]
    )


class LogSpendingForm(Form):
    amount = DecimalField(
        'Amount',
        validators=[InputRequired(), NumberRange(min=0, max=100000000)]
    )
    account = SelectField(
        'Account',
        coerce=str,
        validators=[InputRequired()]
    )
    date = DateField(
        'Date of Spending',
        format='%Y-%m-%d',
        default=datetime.now().date(),
        validators=[InputRequired()]
    )
    description = StringField(
        'Description',
        validators=[Length(max=200)]
    )
    spending_type = SelectField(
        'Spending Type',
        coerce=str,
        validators=[InputRequired()]
    )


class AddAccountForm(Form):
    account = StringField(
        'Account',
        validators=[InputRequired(), Length(max=255)]
    )


class CreateReportForm(Form):
    filename = StringField(
        'Filename',
        validators=[Length(max=200)]
    )
