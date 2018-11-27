from project import app
from project.controllers.forms import SignupForm
from project.models.User import User
from project.models.UserInformation import UserInformation
from project.models.Address import Address
from flask import render_template, redirect, url_for, request, flash
from flask.views import View
from project import db
from project import bcrypt


class SignupController(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        """
        Signup handler. Takes form data and creates a new user

        :return: Template
        """
        form = SignupForm(request.form)
        form.state.choices = [(state, state) for state in
                              ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                               'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD',
                               'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                               'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                               'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY')]
        if request.method == 'POST' and form.validate_on_submit():
            info = UserInformation(int(form.income.data),
                                   Address(form.street_address.data,
                                           form.city.data,
                                           form.state.data,
                                           form.zip.data))
            password = bcrypt.generate_password_hash(form.password.data)
            user = User(form.email.data, password, info)
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            return redirect(url_for('login'))
        return render_template('signup.html', form=form)


app.add_url_rule('/signup', view_func=SignupController.as_view('signup'))
